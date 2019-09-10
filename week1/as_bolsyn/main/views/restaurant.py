from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Restaurant
from main.serializers import RestaurantSerializer


class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantCreate(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Restaurant.objects.for_user(self.request.user)
