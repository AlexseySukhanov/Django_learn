from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def credits(request):
    return render(request, 'generator/credits.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRSTUWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_'))

    length = int(request.GET.get('length',12))
    thepass=''
    for x in range(length):
        thepass +=random.choice(characters)

    #thepass = ''
    return render(request, 'generator/password.html', {'password':thepass})
