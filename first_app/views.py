from django.shortcuts import render

# Create your views here.
def content(request):
    return render(request, './first_app/content.html')
def home(request):
    return render(request, "./first_app/home.html")