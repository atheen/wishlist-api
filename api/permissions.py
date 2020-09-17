from rest_framework.permissions import BasePermission
#from django.utils import timezone
class IsOwner(BasePermission):
    message = "go away"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False
