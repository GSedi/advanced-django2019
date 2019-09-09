from django.urls import path
from main.views import RestaurantList, RestaurantDetail, MenuList, MenuDetail, MenuItemList, MenuItemDetail

urlpatterns = [
    path('restaurants/', RestaurantList.as_view()),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view()),
    path('restaurants/<int:restaurant_id>/menus/', MenuList.as_view()),
    path('menus/<int:pk>/', MenuDetail.as_view()),
    path('menus/<int:menu_id>/menu_items/', MenuItemList.as_view()),
    path('menu_items/<int:pk>/', MenuItemDetail.as_view()),
]
