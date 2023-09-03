from django.shortcuts import render
from PIL import Image
from .encoder import encode
from .decoder import decode
from .models import ImageUploadModel
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def encoder_view(request):
    if request.method == 'POST':
        code = request.POST.get("user_code")
        image = encode(code)
        image.save("media/result.png")
    return render(request, 'encoder-result.html')


def decoder_view(request):
    if request.method == 'POST':
        image = request.FILES["code_image"]
        print(image)
        obj, created = ImageUploadModel.objects.get_or_create(pk=1)
        obj.image = image
        obj.save()
        img_path = "media/"+ str(obj.image)
       
        decoded = decode(Image.open(img_path))
        os.remove(img_path)
    
        print(decoded)
    return render(request,'decoder-result.html',{
        'decoded':decoded
    })