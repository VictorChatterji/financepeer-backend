from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class JdataSerializer(serializers.ModelSerializer):
    class Meta:
       model = Jdata
       fields = ('id', 'userId', 'title', 'body')