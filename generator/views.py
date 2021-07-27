from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html',)

def about(request):
    return render(request,'generator/about.html',)      

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    special = list('!@#$%^&*+=')
    numbers = list("1234567890")

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(special)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    length = int(request.GET.get('length',12))

    thepassword = ''

    if length < 0 or length > 14:
         return HttpResponse('<h1>WRONG LENGTH</h1>')
    for x in range(length):
        thepassword+= random.choice(characters)


    return render(request,'generator/password.html',{'password': thepassword})