# Generated by Django 3.1 on 2020-08-27 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0005_remove_homepageslider_alt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Page`s'},
        ),
        migrations.RemoveField(
            model_name='homepageslider',
            name='image',
        ),
        migrations.AddField(
            model_name='homepageslider',
            name='slide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
