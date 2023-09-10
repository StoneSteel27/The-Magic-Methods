from rest_framework import serializers


class CodeSerializer(serializers.Serializer):
    """Implements CodeSerializer"""

    user_code = serializers.CharField()


class ImageUploadSerializer(serializers.Serializer):
    """Implements ImageUploadSerializer"""

    code_image = serializers.ImageField()
