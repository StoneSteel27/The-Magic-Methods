import os
import base64
from io import BytesIO
from django.shortcuts import render
from PIL import Image

from code_stego import decode, encode



# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def encoder_view(request):
    if request.method == "POST":
        code = request.POST.get("user_code")
        image = encode(code) 
        image_data = BytesIO()
        image.save(image_data, format="PNG")  # Save the image to a BytesIO buffer in PNG format
        image_data.seek(0)

        # Encode the image data as a base64 string
        image_base64 = base64.b64encode(image_data.read()).decode("utf-8")

        return render(request, "encoder-result.html", {"image_base64": image_base64})

    return render(request, "encoder-result.html")


def decoder_view(request):
    if request.method == "POST":
        image = request.FILES["code_image"]
        # Decode the image directly from memory
        with BytesIO(image.read()) as img_buffer:
            img = Image.open(img_buffer)
            decoded = decode(img)

    return render(request, "decoder-result.html", {"decoded": decoded})
