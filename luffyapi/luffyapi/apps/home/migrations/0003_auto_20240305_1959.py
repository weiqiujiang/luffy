# Generated by Django 2.2.5 on 2024-03-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240305_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.ImageField(max_length=255, upload_to='banner', verbose_name='广告图片'),
        ),
    ]
