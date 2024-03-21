from django.db import models


# Create your models here.
class UserProfile(models.Model):
    login = models.CharField(max_length=25, unique=True, verbose_name='Inter login')
    password = models.CharField(max_length=25, verbose_name='Inter password')
    email = models.EmailField()
    name = models.CharField(max_length=25, unique=True, verbose_name='Inter name')
    author = models.BooleanField(default=False, verbose_name='Can posts')
    avatar = models.ImageField(upload_to='images/', verbose_name="Load user avatar", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
