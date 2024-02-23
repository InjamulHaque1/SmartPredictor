from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username

