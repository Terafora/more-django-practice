from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("My name is Charlotte. I'm a multi-lingual full-stack web developer. Autumn is my favourite season and I hope to go back to swimming most days of the week after I finally have my ops.")