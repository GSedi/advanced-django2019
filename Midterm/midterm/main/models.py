from django.db import models
from main import constants


class ProductServiceBase(models.Model):
    name = models.CharField(max_length=21)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(ProductServiceBase):
    size = models.IntegerField()
    type = models.PositiveSmallIntegerField(choices=constants.PRODUCT_TYPES, default=constants.TYPE_ONE)
    existence = models.BooleanField(default=True)


class Service(ProductServiceBase):
    approximate_duration = models.PositiveIntegerField()
    service_type = models.PositiveSmallIntegerField(choices=constants.SERVICE_TYPES, default=constants.TYPE_ONE)