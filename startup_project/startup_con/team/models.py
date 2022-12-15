from codecs import unicode_escape_decode
from enum import unique
from turtle import position
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100,)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/%Y/%m/%d/')
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SocMedia(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='socmedia/%Y/%m/%d/', blank=True, null=True)
    link = models.URLField(max_length = 200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name