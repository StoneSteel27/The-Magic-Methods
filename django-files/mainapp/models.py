from django.db import models


# Create your models here.
class ImageUploadModel(models.Model):
    image = models.FileField(upload_to="decoding")
