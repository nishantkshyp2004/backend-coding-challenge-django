from rest_framework import permissions


class NoteTakingPermissions(permissions.BasePermission):
    """
    NoteTaking permission class
    """

    def has_permission(self, request, view):
        """
        Check if the request is in SAFE_METHODS('GET', 'HEAD', 'OPTIONS') or
        user is authenticated.
        :param request: Request object
        :param view: View
        :return:Boolean(True or False)
        """
        return bool(request.method in permissions.SAFE_METHODS or
                    (request.user and request.user.is_authenticated))

    def has_object_permission(self, request, view, obj):
        """
        Method to check the object permission for every kind of
        rest api request i.e get, post, put, delete,
        head or options.

        :param request: Request object.
        :param view: view.
        :param obj: Object
        :return: Boolean (True or False)
        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # If condition will staify the request those are not in
        # SAFE_METHODS(GET, HEAD or OPTIONS)
        # If visibility is public and owner is not the request
        # user then obj should be only rendered,
        # and shouldn`t be allowed to amend the records.
        if obj.visibility == "public" and obj.owner != request.user:
            return False

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class UserPermissions(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        return bool(request.method in permissions.SAFE_METHODS or
                    (request.user and request.user.is_authenticated)

                    )

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user
