from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(User):
    gender = models.CharField(null=True, blank=True, max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    author = models.BooleanField(null=True, blank=True, default=False, verbose_name='Can posts')
    avatar = models.ImageField(upload_to='images/', verbose_name="Load user avatar", null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    social = models.URLField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True, default=0)
