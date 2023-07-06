from django.shortcuts import render
import random

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generate = ''
    
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-_+/'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        generate += random.choice(characters)
        
    return render(request, 'password.html', {'password': generate})

'''
def save(request):
    saved = []
    if request.GET.get('save'):
        saved += password +'\n'
    
    return render(request, 'save.html', {'save':saved})
    '''