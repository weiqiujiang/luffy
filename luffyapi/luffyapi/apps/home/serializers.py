# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/3/4 21:55

from rest_framework import serializers
from .models import Banner


class BannerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ['image_url', 'link']