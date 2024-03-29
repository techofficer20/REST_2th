from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_objects_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            return True
        else:
            return False
        