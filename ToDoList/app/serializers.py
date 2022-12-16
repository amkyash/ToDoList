from rest_framework import serializers
from .models import *


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('Title','Date','Completed')