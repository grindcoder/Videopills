# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render
from video_manager.models import VideoContainer
from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    # TODO gabri
    # Non prendere tutti i video pills ma solo gli ultimi 6 che sono stati inseriti
    # in ordine temporale
    pills= VideoContainer.objects.all().order_by('pub_date')[:6]
    return render_to_response('home/home.html', {"list_of_pills":pills} )

def redirect_to_videopills():
    return "fuck"



