from django.shortcuts import render
from .encoder import encode
from .decoder import decode

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
    return render(request, 'result.html')