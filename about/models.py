from django.db import models

from wagtail.core.models import Page 
from wagtail.core.fields import StreamField , RichTextField
from wagtail.admin.edit_handlers import FieldPanel , StreamFieldPanel , ObjectList  ,TabbedInterface

from myapp import blocks
# Create your models here.


class AboutPage(Page):
    template = "about/about_page.html"

    banner_header = models.CharField(max_length=50 , null=True , blank=False)
    banner_content = RichTextField()

    content = StreamField(
        [
            ("employees" , blocks.EmployeeCardBlock() )
        ],
        blank=True,
        null=True
    )

    banner_panels = [
        FieldPanel("banner_header"),
        FieldPanel("banner_content")
    ]


    content_panels =  Page.content_panels+ [
        StreamFieldPanel("content")
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels , heading="Content"),
        ObjectList(banner_panels , heading="Banner"),
        ObjectList(Page.promote_panels , heading="Promote"),
        ObjectList(Page.settings_panels , heading="Settings")
    ])

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page`s"