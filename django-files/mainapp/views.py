from django.shortcuts import render


# Rendering the home page
def index(request):
    """Renders index"""
    return render(request, "index.html")


# Rendering the about page
def about(request):
    """Renders about"""
    return render(request, "about.html")
