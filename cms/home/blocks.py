import wagtail
import wagtail.images
from rest_framework import serializers
from wagtail.images.blocks import ImageChooserBlock


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wagtail.images.get_image_model()
        fields = ["title", "file", "width", "height", "file_size"]


class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return ImageSerializer(context=context).to_representation(value)
