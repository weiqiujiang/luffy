# -*- coding: utf-8 -*-
# @Author: weiqiujiang
# @Date: 2024/3/6 9:32
from django.db import models


class BaseModel(models.Model):
    is_show = models.BooleanField(default=False, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name='排序')
    id_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        # 数据迁移时不创建表
        abstract = True
