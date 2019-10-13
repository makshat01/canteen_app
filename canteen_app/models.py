from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    phone = models.CharField(max_length=12, blank=True)


class FoodType(models.Model):

    food_type = models.CharField(max_length=100)
    image = models.FileField(null=True)

    def __str__(self):
        return self.food_type


class Menu(models.Model):

    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.food_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_fulfilled = models.BooleanField(default=False)
    total_price = models.PositiveSmallIntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()