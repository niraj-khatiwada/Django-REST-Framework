from rest_framework import permissions


class BlackListPermission(permissions.BasePermission):
    message = "Your api request count exceeded limit. Try againa after 24hrs"

    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        print(ip_address)
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = " You are not authenticated to perform this task"

    # def has_permission(self, request, view):
    #     return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
