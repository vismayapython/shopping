from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')


