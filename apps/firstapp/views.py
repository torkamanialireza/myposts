from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
# Create your views here.
def index(request):

    return render(request, "firstapp/index.html",{'notes': Note.objects.all()})


def create(request):
    note = Note.objects.create(note = request.POST['note'])
    last =  Note.objects.last()
    content = {
    'notes': Note.objects.all(),
    'last':last
    }
    return render(request, "firstapp/all.html" ,content)
def all(request):
    last =  Note.objects.last()
    content = {
    'notes': Note.objects.all(),
    'last':last
    }
    return render(request, 'firstapp/all.html', content)
