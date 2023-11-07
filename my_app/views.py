from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("My name is Charlotte. I'm a multi-lingual full-stack web developer. Autumn is my favourite season and I hope to go back to swimming most days of the week after I finally have my ops.")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")

def add(request, num1, num2):
    return HttpResponse(f"{num1 + num2}")