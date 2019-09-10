from django.urls import path
from main.views.restaurant import RestaurantList, RestaurantCreate, RestaurantDetail
from main.views.menu import MenuList, MenuCreate, MenuDetail
from main.views.menu_item import MenuItemList, MenuItemCreate, MenuItemDetail


urlpatterns = [
    path('restaurants/list/', RestaurantList.as_view()),
    path('restaurants/create/', RestaurantCreate.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view()),
    path('restaurants/<int:restaurant_id>/menus/list/', MenuList.as_view()),
    path('restaurants/<int:restaurant_id>/menus/create/', MenuCreate.as_view()),
    path('menus/<int:pk>/', MenuDetail.as_view()),
    path('menus/<int:menu_id>/menu_items/list/', MenuItemList.as_view()),
    path('menus/<int:menu_id>/menu_items/create/', MenuItemCreate.as_view()),
    path('menu_items/<int:pk>/', MenuItemDetail.as_view()),
]
