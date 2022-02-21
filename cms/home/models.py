from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.api import APIField
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from .blocks import APIImageChooserBlock


class HomePage(Page):
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", APIImageChooserBlock()),
            (
                "two_columns",
                blocks.StreamBlock(
                    [
                        ("text", blocks.RichTextBlock()),
                    ],
                    min_num=2,
                    max_num=2,
                ),
            ),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    api_fields = [
        APIField("body"),
    ]
