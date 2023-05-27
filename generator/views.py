from django.shortcuts import render
import random

def generator(request):
    return render(request, "generator.html")

def password(request):

    characters = list('abcchdefghijklmnñopqrstuvwxyz')
    generator_password = ''

    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDFJIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!"#/.-,$+%*&)_:'))
    if request.GET.get('numbers'):
        characters.extend(list('0987654321'))

    for i in range(length):
        generator_password += random.choice(characters)

    return render(request, 'password.html', {'password': generator_password})


