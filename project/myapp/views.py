from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
import numpy as np
from .models import UserProfile, House
from .forms import UserProfileForm, UserForm
import logging
from django.shortcuts import render
from django.http import JsonResponse
from scripts.predict import predict


def load_profile_picture(request):
    user_profile = UserProfile.objects.get(user=request.user)
    profile_picture_url = user_profile.profile_picture.url if user_profile.profile_picture else ''
    return JsonResponse({'profile_picture_url': profile_picture_url})

def home(request):
    return render(request, 'home.html')
   
def login(request):
    if request.method == 'POST':
        username = request.POST.get("u_name")
        password = request.POST.get("u_password")
        
        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:
            auth_login(request, authenticated_user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


logger = logging.getLogger(__name__)
def send_otp_email(email, otp):
    try:
        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        sender_email = settings.EMAIL_FROM
        recipient_list = [email]

        send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
        logger.info(f"OTP sent to {email}")
        
    except Exception as e:
        logger.error(f"Error sending OTP to {email}: {e}")

def register(request):
    if request.method == 'POST':
        u_name = request.POST.get("u_name")
        u_fname = request.POST.get("u_fname")
        u_lname = request.POST.get("u_lname")
        u_email = request.POST.get("u_email")
        u_password = request.POST.get("u_password")
        u_age = request.POST.get("u_age")
        u_address = request.POST.get("u_address")
        u_mobile = request.POST.get("u_mobile")
        u_gender = request.POST.get("u_gender")  # Get the uploaded profile picture

        # Check if username or email already exists
        if User.objects.filter(username=u_name).exists() or User.objects.filter(email=u_email).exists():
            messages.error(request, "Username or email already exists.")
            return redirect("register")

        otp_generated = get_random_string(length=6, allowed_chars='1234567890')
        send_otp_email(u_email, otp_generated)
        print(otp_generated)
        
        # Save data in session
        request.session['u_name'] = u_name
        request.session['u_fname'] = u_fname
        request.session['u_lname'] = u_lname
        request.session['u_email'] = u_email
        request.session['u_password'] = u_password
        request.session['u_age'] = u_age
        request.session['u_address'] = u_address
        request.session['u_mobile'] = u_mobile
        request.session['u_gender'] = u_gender
        request.session['otp_generated'] = otp_generated  
        
        return redirect('verify_otp')
    
    return render(request, 'register.html')

def verify_otp(request):
    u_email = request.session.get('u_email')
    if request.method == 'POST':
        
        otp_entered = request.POST.get('otp')
        otp_generated = request.session.get('otp_generated')  
        
        u_name = request.session.get('u_name')
        u_fname = request.session.get('u_fname')
        u_lname = request.session.get('u_lname')
        u_email = request.session.get('u_email')
        u_password = request.session.get('u_password')
        u_age = request.session.get('u_age')
        u_address = request.session.get('u_address')
        u_mobile = request.session.get('u_mobile')
        u_gender = request.session.get('u_gender')

        if otp_entered == otp_generated:
            user = User.objects.create_user(username=u_name, first_name=u_fname, last_name=u_lname, email=u_email, password=u_password)
            user_profile = UserProfile(user=user, age=u_age, address=u_address, mobile=u_mobile, gender=u_gender)
            user_profile.save()
            
            authenticated_user = authenticate(request, username=u_name, password=u_password)
            if authenticated_user is not None:
                auth_login(request, authenticated_user) 
                messages.success(request, "Your account has been successfully created.")
                return redirect("home")
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return render(request, 'verify_otp.html', {'email': u_email, 'otp_generated': otp_generated})
        
    return render(request, 'verify_otp.html', {'email': u_email})

def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    profile_form = UserProfileForm(instance=user_profile)
    user_form = UserForm(instance=request.user)
    
    if request.method == "POST":
        if "delete_account" in request.POST:
            request.user.delete()
            auth_logout(request)
            messages.success(request, "Your account has been deleted.")
            return redirect('login')

        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        user_form = UserForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user  # Ensure the user is associated with the profile
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']  # Handle profile picture upload
            profile.save()
            user_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('user_profile')
        else:
            messages.error(request, "Error updating profile. Please check the form.")
    
    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'user_profile.html', context)

@login_required
def logout(request):
    user = request.user
    auth_logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')

def houses(request):
    houses = House.objects.all()
    context = {
        'houses': houses,
    }
    return render(request, 'houses.html', context)

def detailBody(request, house_id=None):
    if house_id is not None:
        house = get_object_or_404(House, id=house_id)
        context = {
            'house': house,
        }
        return render(request, 'detailBody.html', context)
    else:
        return HttpResponse("House ID not provided!")


def prediction(request):
    if request.method == 'POST':
        total_rooms = int(request.POST.get('Total Room'))
        bedrooms = int(request.POST.get('Bedroom'))
        bathrooms = int(request.POST.get('Bathroom'))
        car_parking = int(request.POST.get('Car Parking'))
        area_size = float(request.POST.get('Area Size in Sq.Feet'))
        
        predicted_price = predict(total_rooms, bedrooms, bathrooms, car_parking, area_size)

        if isinstance(predicted_price, (list, np.ndarray)) and len(predicted_price) > 0:
            result = predicted_price[0]  
        else:
            result = predicted_price 
            
        return render(request, 'prediction.html', {'result': result})
    else:
        return render(request, 'prediction.html')


def about_us(request):
    return render(request, 'about_us.html')