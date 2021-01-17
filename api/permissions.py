from rest_framework import permissions 


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Read permission are allowed to any request, GET, HEAD and OPTIONS are safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        #write permission are only allowed by the owner of the snippet
        return obj.owner == request.user