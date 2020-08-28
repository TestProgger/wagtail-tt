from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    ObjectList,
    TabbedInterface
)
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    template = "home/home_page.html"
    ############## Banner Fields #################

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+"
    )

    ##############  Panels  ###################
    slider_title = models.CharField(max_length=80, null=True, blank=False)
    slider_panels = [
        FieldPanel("slider_title"),
        MultiFieldPanel([
            InlinePanel("slider_images", max_num=6, min_num=1, label="Slide")
        ],
            heading="Slider Images"
        ),

    ]

    banner_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Settings"
        )
    ]

    content_panels = Page.content_panels + [
       
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(slider_panels, heading="Slider"),
            ObjectList(banner_panels,  heading="Banner"),
            ObjectList(Page.promote_panels, heading='Promote'),
            ObjectList(Page.settings_panels, heading='Settings'),
        ]
    )

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page`s"


class HomePageSlider(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name="slider_images")
    slide = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=False, related_name="+")

    panels = [
        ImageChooserPanel("slide"),
    ]
