# Generated by Django 3.1 on 2020-08-28 10:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200828_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('posts', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('content', wagtail.core.blocks.RichTextBlock(required=True)), ('background_type', wagtail.core.blocks.ChoiceBlock(choices=[('bg-primary', 'Primary (Black)'), ('bg-secondary', 'Secondary (Grey)'), ('bg-success', 'Success (Green)'), ('bg-danger', 'Danger (Red)'), ('bg-warning', 'Warning (Yellow)'), ('bg-info', 'Info (Blue) ')])), ('date', wagtail.core.blocks.DateTimeBlock(required=True))])))]))], blank=True, null=True),
        ),
    ]
