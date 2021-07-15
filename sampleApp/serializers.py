# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 23:58:09 2021

@author: Phuah
"""

from rest_framework import serializers
from . models import user

#serializers converts to JSON format
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        #fields = '__all__'
        fields = ('email','username','role')