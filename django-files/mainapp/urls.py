from django.urls import include, path

from . import views
from .api_views import EncoderAPIView,DecoderAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("stego/",views.stego,name='stego'),
    path("encode/", views.encoder_view, name="encode"),
    path("decode/", views.decoder_view, name="decode"),

    path('api/encode/', EncoderAPIView.as_view(), name='encode-api'),
    path('api/decode/', DecoderAPIView.as_view(), name='decode-api'),
]
