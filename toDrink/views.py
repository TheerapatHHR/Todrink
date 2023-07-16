from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import * 
# Create your views here.

def home(request):
    context = {}

    return render(request, 'toDrink/home.html', context)

def history(request):
    text = "No history"
    context = {'text':text}

    return render(request, 'toDrink/history.html', context)