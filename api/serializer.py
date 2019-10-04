from rest_framework import serializers

from api.models import *


class groupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = group
        fields = ('groupName', 'config')


class devicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = devices
        fields = ('uuid', 'group', 'hashes')

class configurationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = config
        fields = ('name', 'config')


class zipFilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = zipFiles
        fields = ('zipfile', 'device')

