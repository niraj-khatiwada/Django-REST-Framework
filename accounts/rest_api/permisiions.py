from rest_framework import permissions


class BlackListPermission(permissions.BasePermission):
    message = "Your api request count exceeded limit. Try againa after 24hrs"

    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        print(ip_address)
        return False
