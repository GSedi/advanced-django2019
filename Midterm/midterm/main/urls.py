from rest_framework.routers import DefaultRouter

from main.views import ProductViewSet, ServiceViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, base_name='main')
router.register('services', ServiceViewSet, base_name='main')

urlpatterns = router.urls
