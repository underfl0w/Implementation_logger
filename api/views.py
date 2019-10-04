from __future__ import unicode_literals

import threading

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializer import *
from scripts import csvLogic


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

    def create(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        x = threading.Thread(target=csvLogic.saveHashes, args=(request.data['zipfile'], request.data['device']))
        x.start()
        a= self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(a.id, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        return serializer.save()


