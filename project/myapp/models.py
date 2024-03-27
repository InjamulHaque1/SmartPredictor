from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class UserProfile(models.Model):
    def __str__(self):
        return self.fullname()
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    

@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        profile = UserProfile.objects.get(user=instance)
        profile.delete()
    except UserProfile.DoesNotExist:
        pass

class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class House(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="house_imgs", null=True)
    spec = models.TextField()
    price = models.PositiveBigIntegerField()
    detail = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    