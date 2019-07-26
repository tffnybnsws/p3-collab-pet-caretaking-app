from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def user1(request):
    return render(request, 'draw/user1.html', {})

def variant(request):
    return render(request, 'draw/variant.html', {})
