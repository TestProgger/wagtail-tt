# Generated by Django 3.1 on 2020-08-27 21:35

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20200827_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=wagtail.core.fields.StreamField([('employees', wagtail.core.blocks.StructBlock([('employees_title', wagtail.core.blocks.CharBlock(help_text='Add employee`s title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('post', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('full_name', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('desription', wagtail.core.blocks.RichTextBlock(max_length=255, required=True)), ('background_type', wagtail.core.blocks.ChoiceBlock(choices=[('bg-primary', 'Primary (Black)'), ('bg-secondary', 'Secondary (Grey)'), ('bg-success', 'Success (Green)'), ('bg-danger', 'Danger (Red)'), ('bg-warning', 'Warning (Yellow)'), ('bg-info', 'Info (Blue) ')]))])))]))], blank=True, null=True),
        ),
    ]
