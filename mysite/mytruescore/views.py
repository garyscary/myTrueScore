from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return HttpResponse("Hello, world. You're at the polls index.")