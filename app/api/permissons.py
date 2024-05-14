from rest_framework.permissions import BasePermission,SAFE_METHODS
from rolepermissions.checkers import has_role
from .roles import AdminRole,SalesPersonRole,ClientRole
class HavePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and has_role(request.user,ClientRole) or has_role(request.user,SalesPersonRole):
            return True
        if has_role(request.user,AdminRole) and request.method in ['POST','PUT','DELETE']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if has_role(request.user,AdminRole):
            return True
        return False
    
class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if has_role(request.user,AdminRole):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if has_role(request.user,AdminRole):
            return True
        return False