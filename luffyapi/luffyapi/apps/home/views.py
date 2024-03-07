from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Banner, Nav
from .serializers import BannerModelSerializer, NavModelSerializer
from luffyapi.settings import constans


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, id_deleted=False).order_by('-orders', '-id')[:constans.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, id_deleted=False, position=1).order_by('-orders', '-id')[:constans.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, id_deleted=False, position=2).order_by('-orders', '-id')[:constans.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
