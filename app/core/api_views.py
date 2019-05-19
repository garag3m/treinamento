from rest_framework import viewsets, permissions

from . import models
from . import serializers as serializers


# UUIDUser viewset
# - - - - - - - - - - - - - - - - - - -
class UUIDUserViewSet(viewsets.ModelViewSet):

    queryset = models.UUIDUser.objects.all()
    serializer_class = serializers.UUIDUserSerializer

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return models.Environment.objects.all()
    #     return models.Environment.objects.filter(group__in=self.request.user.groups.all())

    # def get_serializer_class(self):
    #     if self.request.user.is_superuser:
    #         return serializers.EnvironmentCreateSerializer
    #     return serializers.EnvironmentSerializer