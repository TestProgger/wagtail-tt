# Generated by Django 3.1 on 2020-08-27 20:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_header', models.CharField(max_length=50, null=True)),
                ('banner_content', wagtail.core.fields.RichTextField()),
                ('content', wagtail.core.fields.StreamField([('employees', wagtail.core.blocks.StructBlock([('employees_title', wagtail.core.blocks.CharBlock(help_text='Add employee`s title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('post', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('desription', wagtail.core.blocks.TextBlock(max_length=255, required=True)), ('bg_type', wagtail.core.blocks.ChoiceBlock(choices=[('bg-primary', 'Primary (Black)'), ('bg-secondary', 'Secondary (Grey)'), ('bg-success', 'Success (Green)'), ('bg-dander', 'Dander (Red)'), ('bg-warning', 'Warning (Yellow)'), ('bg-info', 'Info (Blue) ')]))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Page`s',
            },
            bases=('wagtailcore.page',),
        ),
    ]