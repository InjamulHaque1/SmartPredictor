from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [    
    # Basic urls           
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    
    # User account urls
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('load_profile_picture/', views.load_profile_picture, name='load_profile_picture'),
    
    # Houses urls
    path('detailBody/<int:house_id>/', views.detailBody, name='detailBody'),
    path('houses/', views.houses, name='houses'),
    
    # Prediction urls
    path('prediction/', views.prediction, name='prediction'),
    
    # Error handaling urls
    path('custom_error/', views.custom_error, name='custom_error'),
    path('<path:undefined_path>/', RedirectView.as_view(url='/custom_error/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)