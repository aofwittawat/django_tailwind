from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'blog_app/home.html')


