from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel , StreamFieldPanel

from myapp import blocks

# Create your models here.

class BlogPage(Page):

    template = "blog/blog_page.html"
    
    content = StreamField(
        [
            ('posts' , blocks.BlogCardBlock())
        ],
        blank = True,
        null=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Page`s"