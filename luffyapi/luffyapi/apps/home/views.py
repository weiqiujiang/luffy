from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from luffyapi.settings import constans


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, id_deleted=False).order_by('-orders', '-id')[:constans.BANNER_LENGTH]
    serializer_class = BannerModelSerializer
