from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from api.serializer import *

class groupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = group.objects.all()
    serializer_class = groupSerializer

class devicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows machines to be viewed or edited
    """
    queryset = devices.objects.all()
    serializer_class = devicesSerializer


class configurationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configurations to be viewed or edited
    """
    queryset = config.objects.all()
    serializer_class = configurationSerializer

class zipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows base64 encoded zips to be viewed.
    """
    queryset = zipFiles.objects.all()
    serializer_class = zipFilesSerializer

