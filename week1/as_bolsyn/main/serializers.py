from rest_framework import serializers
from main.models import Restaurant, Menu, MenuItem
from auth_.serializers import UserSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
