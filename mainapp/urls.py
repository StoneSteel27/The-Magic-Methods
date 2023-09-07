from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("encode/", views.encoder_view, name="encode"),
    path("decode/", views.decoder_view, name="decode"),
]
