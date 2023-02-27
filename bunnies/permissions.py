from rest_framework import permissions


class RabbitHolePermissions(permissions.BasePermission):
    """
    Custom permission class for RabbitHole views that only allows authenticated users to create, update or delete a RabbitHole
    object, and only allows the owner of a RabbitHole object to view, update or delete it.
    """

    def has_permission(self, request, view):
        """
        Check if the requesting user has permission to perform the requested action on a collection of RabbitHole objects.
        """
        if request.method in permissions.SAFE_METHODS:
            # Allow any user to read the collection of RabbitHole objects
            return super().has_permission(request, view)
        # Allow only authenticated users to create, update or delete a RabbitHole object
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user has permission to perform the requested action on a single RabbitHole object.
        """
        if request.method in permissions.SAFE_METHODS:
            # Allow any user to read a single RabbitHole object
            return super().has_object_permission(request, view, obj)
        # Allow only the owner of the RabbitHole object to update or delete it
        return request.user == obj.owner
