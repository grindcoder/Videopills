# -*- coding: utf-8 -*-
import datetime
from video_manager.models import VideoContainer
from django.shortcuts import render_to_response
# Create your views here.


def home(request):
    # TODO gabri
    # Non prendere tutti i video pills ma solo gli ultimi 6 che sono stati inseriti
    # in ordine temporale
    pills= VideoContainer.objects.all().order_by('-pub_date')[:6]
    return render_to_response('home/home.html', {"list_of_pills":pills} )

def redirect_to_videopills():
    return "fuck"


def search(request):
     query_string = ''
     found_entries = None
     if ('q' in request.GET) and request.GET['q'].strip():
         query_string = request.GET['q']

         entry_query = get_query(query_string, ['title', 'body',])

         found_entries = VideoContainer.objects.filter(entry_query).order_by('-pub_date')

     return render_to_response('search_page/search_page.html',
                           { 'query_string': query_string, 'found_entries': found_entries },)


