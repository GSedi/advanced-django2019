from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import Restaurant, Menu, MenuItem
from main.serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer


class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)


class MenuList(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    lookup_field = 'restaurant_id'

    def get_queryset(self):
        restaurant = Restaurant.objects.get(pk=self.kwargs[self.lookup_field])
        return restaurant.menus.all()

    def perform_create(self, serializer):
        restaurant = Restaurant.objects.get(pk=self.kwargs[self.lookup_field])
        serializer.save(restaurant=restaurant)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemList(generics.ListCreateAPIView):
    serializer_class = MenuItemSerializer
    lookup_field = 'menu_id'

    def get_queryset(self):
        menu = Menu.objects.get(pk=self.kwargs[self.lookup_field])
        return menu.menu_items.all()

    def perform_create(self, serializer):
        menu = Menu.objects.get(pk=self.kwargs[self.lookup_field])
        serializer.save(menu=menu)


class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
