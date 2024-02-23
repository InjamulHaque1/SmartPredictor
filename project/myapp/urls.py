from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [    
    #admin and basic urls
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('houses/', views.houses, name='houses'),
    path('prediction/', views.prediction, name='prediction'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
