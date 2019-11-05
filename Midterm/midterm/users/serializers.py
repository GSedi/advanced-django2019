from rest_framework import serializers
from users.models import MainUser, Profile
from django.db import transaction


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'password', 'profile')

    def create(self, validated_data):
        with transaction.atomic():
            print(validated_data)
            profile_data = validated_data.pop('profile')
            user = MainUser.objects.create_user(**validated_data)
            Profile.objects.create(user=user, **profile_data)
            return user
