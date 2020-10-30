from rest_framework.permissions import BasePermission, SAFE_METHODS
"""
API V1: Accounts Permissions
"""
###
# Libraries
###


###
# Permissions
###
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
