from django.urls import include, path

from . import views
from .api_views import EncoderAPIView,DecoderAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

    path('api/encode/', EncoderAPIView.as_view(), name='encode-api'),
    path('api/decode/', DecoderAPIView.as_view(), name='decode-api'),
]
