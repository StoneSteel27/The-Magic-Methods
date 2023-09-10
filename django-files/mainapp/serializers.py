from rest_framework import serializers

class CodeSerializer(serializers.Serializer):
    user_code = serializers.CharField()


class ImageUploadSerializer(serializers.Serializer):
    code_image = serializers.ImageField()
