# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    return render_to_response('home/home.html')

def redirect_to_videopills():
    return "fuck"