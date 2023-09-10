from django.shortcuts import render

# Rendering the home page
def index(request):
    return render(request, "index.html")

# Rendering the about page
def about(request):
    return render(request, "about.html")


