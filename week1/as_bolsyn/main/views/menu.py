from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Restaurant, Menu
from main.serializers import MenuSerializer


class MenuList(generics.ListAPIView):
    serializer_class = MenuSerializer
    lookup_field = 'restaurant_id'

    def get_queryset(self):
        restaurant = Restaurant.objects.get(pk=self.kwargs[self.lookup_field])
        return restaurant.menus.all()


class MenuCreate(generics.CreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )
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
    permission_classes = (IsAuthenticated, )
