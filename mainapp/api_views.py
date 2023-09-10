import base64
from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CodeSerializer, ImageUploadSerializer
from code_stego import decode, encode

#API view to handle the encoding to image
class EncoderAPIView(APIView):
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data.get("user_code")
            # Try block to catch any Errors from encode function
            try:    
                image = encode(code)
                image_data = BytesIO()
                image.save(image_data, format="PNG")
                image_data.seek(0)

                # Encode the image data as a base64 string
                image_base64 = base64.b64encode(image_data.read()).decode("utf-8")

                return JsonResponse({"image_base64": image_base64})
            except Exception as e:
                    Response({"error":e},status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# API view to handle the decoding to code(text)
class DecoderAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            code_image = serializer.validated_data.get("code_image")

            # Try block to catch any Errors from decode function
            try:
                # Decode the image directly from memory
                with BytesIO(code_image.read()) as img_buffer:
                    img = Image.open(img_buffer)
                    decoded = decode(img)

                    return Response({"decoded": decoded}, status=status.HTTP_200_OK)
            except Exception as e:
                Response({"error":e},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
