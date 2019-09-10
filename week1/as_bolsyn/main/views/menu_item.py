from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Menu, MenuItem
from main.serializers import MenuItemSerializer


class MenuItemList(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    lookup_field = 'menu_id'

    def get_queryset(self):
        menu = Menu.objects.get(pk=self.kwargs[self.lookup_field])
        return menu.menu_items.all()


class MenuItemCreate(generics.CreateAPIView):
    serializer_class = MenuItemSerializer
    permission_classes = (IsAuthenticated, )
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
    permission_classes = (IsAuthenticated, )
