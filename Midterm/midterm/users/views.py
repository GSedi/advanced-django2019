from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from users.serializers import UserSerializer, ProfileSerializer
from users.models import MainUser


class RegisterViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = MainUser.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MainUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
