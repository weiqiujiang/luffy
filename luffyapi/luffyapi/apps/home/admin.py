from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Banner, Nav


class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'orders', 'is_show']


class NavModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_show', 'is_site', 'position']


admin.site.register(Banner, BannerModelAdmin)
admin.site.register(Nav, NavModelAdmin)
