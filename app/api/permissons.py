from rest_framework.permissions import BasePermission,SAFE_METHODS
from rolepermissions.checkers import has_role
from .roles import AdminRole,SalesPersonRole,ClientRole
class AccessAdminPanel(BasePermission):
    def has_permission(self, request, view):

        return has_role(request.user, AdminRole) or has_role(request.user, SalesPersonRole) or request.user.is_superuser

class IsClient(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return has_role(request.user, ClientRole) or request.user.is_superuser