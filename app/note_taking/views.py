from note_taking.models import NoteTaking
from note_taking.serializers import NoteTakingSerializer, UserSerializer
from django.contrib.auth.models import User
from note_taking.permissions import NoteTakingPermissions, UserPermissions
from note_taking.filters import CustomSearchFilter
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class NoteTakingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = NoteTaking.objects.all()
    serializer_class = NoteTakingSerializer
    permission_classes = [NoteTakingPermissions]
    filter_backends = [CustomSearchFilter]
    search_fields = ['title', 'body']

    def perform_create(self, serializer):
        """
        Defining the perform_create method to add owner key and its value
        in the validated dict before saving.
        :param serializer: NoteTakind serializer
        :return: None
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Restricts the returned queryset with visibility equal to public
        if user is not authenticated.
        """
        queryset = self.queryset
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(visibility='public')

        return queryset


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request,
                         format=format),
        'notetaking': reverse('notetaking-list', request=request,
                              format=format)
    })
