from rest_framework.permissions import IsAuthenticated


class IsOwnerPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return True
