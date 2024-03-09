# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/3/7 17:27

from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path(r'login/', obtain_jwt_token),
    path(r"captcha/", views.CaptchaAPIView.as_view()),


]
