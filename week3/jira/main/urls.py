from django.urls import path
from main.views import ProjectListAPIView, \
    ProjectDetailAPIView, BlockListView, BlockDetailView, TaskViewSet
from rest_framework import routers

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
    path('blocks/', BlockListView.as_view()),
    path('blocks/<int:pk>/', BlockDetailView.as_view()),
]

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, base_name='main')

urlpatterns += router.urls
