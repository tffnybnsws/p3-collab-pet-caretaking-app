from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def user1(request):
    return render(request, 'draw/user1.html', {})

def user2(request):
    return render(request, 'draw/user2.html', {})

def user3(request):
    return render(request, 'draw/user3.html', {})