from django.shortcuts import render

def index (request):
    name = "amaraa"
    return render (request, 'index.html', {'name': name})