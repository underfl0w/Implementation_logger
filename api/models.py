from django.db import models
import jsonfield

class config(models.Model):
    name = models.CharField(max_length=125)
    config = jsonfield.JSONField()

class group(models.Model):
    groupName = models.CharField(max_length=124)
    config = models.ForeignKey(config, on_delete=models.CASCADE)

class devices(models.Model):
    uuid = models.UUIDField(primary_key=True)
    group = models.ForeignKey(group, on_delete=models.CASCADE)

class zipFiles(models.Model):
    zipfile = models.TextField()
    device = models.ForeignKey(devices, on_delete=models.CASCADE)
