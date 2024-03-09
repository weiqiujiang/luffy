# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/3/7 20:19
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import User


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id': user.id,
        'username': user.username,
    }


def get_user_by_account(account):
    """
    :param account: 可以为username,也可为mobile等等
    :return: user对象
    """
    try:
        user = User.objects.filter(Q(username=account) | Q(mobile=account)).first()
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password) and user.is_authenticated:
            return user
        return None
