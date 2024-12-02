from rest_framework import permissions

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, obj=None):
        if request.method == 'POST':
            return request.user.is_staff
        return True
        
class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTION']:
            return True
        return obj == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTION']:
            return True
        print(obj.owner)
        return obj.owner == request.user