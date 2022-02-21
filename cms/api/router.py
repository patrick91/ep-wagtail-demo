from django.urls import path
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

api_router = WagtailAPIRouter("wagtailapi")


class EPPagesAPIViewSet(PagesAPIViewSet):
    def detail_view(self, request, pk=None, slug=None):
        param = pk

        if slug is not None:
            self.lookup_field = "slug"
            param = slug

        return super().detail_view(request, param)

    @classmethod
    def get_urlpatterns(cls):
        patterns = super().get_urlpatterns()
        return patterns + [
            path("<slug:slug>/", cls.as_view({"get": "detail_view"}), name="detail"),
        ]


api_router.register_endpoint("pages", EPPagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)
