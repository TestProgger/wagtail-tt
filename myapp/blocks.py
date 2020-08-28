from wagtail.core import blocks 
from wagtail.images.blocks import ImageChooserBlock

from django.db import models

BG_TYPE_CHOICES = [
        ('bg-primary' , 'Primary (Black)'),
        ('bg-secondary' , 'Secondary (Grey)'),
        ('bg-success' , 'Success (Green)'),
        ('bg-danger' , 'Danger (Red)'),
        ('bg-warning' , 'Warning (Yellow)'),
        ('bg-info' , 'Info (Blue) ')
    ]

class EmployeeCardBlock( blocks.StructBlock ):
    employees_title = blocks.CharBlock(required=True , help_text="Add employee`s title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("post" , blocks.CharBlock(required=True , max_length=100)),
                ("full_name" , blocks.CharBlock(required=True , max_length=100)),
                ("image", ImageChooserBlock(required=True)),
                ("desription", blocks.RichTextBlock(required=True, max_length=255)),
                ("background_type" , blocks.ChoiceBlock(required=True , choices=BG_TYPE_CHOICES))
            ]
        )
    )

    class Meta:
        template = "blocks/employee_card_block.html"
        icon = "placeholder"
        label = "Employee Cards"



class BlogCardBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("header" , blocks.CharBlock(required=True , max_length=50)),
                ("title" , blocks.CharBlock(required=True , max_length=50)),
                ("content" , blocks.RichTextBlock(required=True)),
                ("background_type" , blocks.ChoiceBlock(required=True , choices=BG_TYPE_CHOICES)),
                ("date" , blocks.DateTimeBlock(required=True ))
            ]
        )
    )

    class Meta:
        template = "blocks/blog_card_block.html"
        icon = "placeholder"
        label = "Blog Posts"