from django.db import models
from django.contrib.auth.models import User


class RestaurantManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Restaurant(models.Model):
    name = models.CharField("Name", max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='restaurants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Menu(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, related_name='menus')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MenuItem(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    price = models.FloatField("Price")
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, related_name='menu_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

