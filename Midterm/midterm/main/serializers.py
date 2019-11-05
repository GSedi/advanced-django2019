from rest_framework import serializers
from main.models import Product, Service


class ProductSerializer(serializers.ModelSerializer):
    size = serializers.IntegerField()

    class Meta:
        model = Product
        fields = '__all__'

    def validate_size(self, value):
        if value < 20 or value > 50:
            raise serializers.ValidationError('size must be greater than 20 lower 50')
        return value


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def validate_approximate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError('approximate duration must be positive')
        return value