from rest_framework import serializers

from . import models


# UUIDUser serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.UUIDUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'cpf')

# UUIDUser serializer
# - - - - - - - - - - - - - - - - - - -
class UUIDUserCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.UUIDUser
        fields = ('pk', 'username', 'first_name', 'last_name', 'cpf', 'password')