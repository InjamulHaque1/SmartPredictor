from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [    
    #admin and basic urls
    path('admin/', admin.site.urls),
    path("houses/", views.houses, name="houses"),
    path('detailBody/<int:house_id>/', views.detailBody, name='detailBody'),
    path('', views.home, name='home'),
    path('houses/', views.houses, name='houses'),
    path('prediction/', views.prediction, name='prediction'),
    path('about_us/', views.about_us, name='about_us'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('houses/', views.houses, name='houses'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)