from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)

    def fullname(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.fullname()
    

@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    try:
        profile = UserProfile.objects.get(user=instance)
        profile.delete()
    except UserProfile.DoesNotExist:
        pass

class Category(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class House(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="house_imgs", null=True)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    area = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    detail = models.TextField()
    spec = models.TextField()
    contact = models.CharField(max_length=200,null=True)
    price = models.PositiveBigIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    