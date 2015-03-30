# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from video_manager.models import VideoContainer
# Create your views here.

def home(request):
    # TODO gabri
    # Non prendere tutti i video pills ma solo gli ultimi 6 che sono stati inseriti
    # in ordine temporale
    pills= VideoContainer.objects.all()
    return render_to_response('home/home.html', {"list_of_pills":pills} )

def redirect_to_videopills():
    return "fuck"