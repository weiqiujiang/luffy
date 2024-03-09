from django.contrib import admin
from .models import User
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'mobile']


admin.site.register(User, UserModelAdmin)