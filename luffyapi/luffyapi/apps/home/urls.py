# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/3/4 22:01

from django.urls import path
from . import views

urlpatterns = [
    path(r'banner/', views.BannerListAPIView.as_view())
]
