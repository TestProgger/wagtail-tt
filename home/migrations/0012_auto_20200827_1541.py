# Generated by Django 3.1 on 2020-08-27 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepage_slider_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_subtitle',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
    ]
