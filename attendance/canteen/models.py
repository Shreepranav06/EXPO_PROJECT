from django.db import models

class Canteen(models.Model):
    name = models.CharField(max_length=100)
    id_canteen = models.IntegerField(default=100)
    password_canteen = models.CharField(max_length=100, default='password')


class Food(models.Model):
    sno = models.IntegerField(default=1)
    food_item = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=100)
    quanity = models.IntegerField(default=1)
