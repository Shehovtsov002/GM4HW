from django.db import models


# Create your models here.
class HouseParser(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BazarParser(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title
