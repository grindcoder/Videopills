# -*- coding: utf-8 -*-
import datetime
from video_manager.models import VideoContainer
from django.shortcuts import render_to_response
import re

from django.db.models import Q
# Create your views here.

def home(request):
    # TODO gabri
    # Non prendere tutti i video pills ma solo gli ultimi 6 che sono stati inseriti
    # in ordine temporale
    pills= VideoContainer.objects.all().order_by('-pub_date')[:6]
    return render_to_response('home/home.html', {"list_of_pills":pills} )

def redirect_to_videopills():
    return "fuck"


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
     query_string = ''
     found_entries = None
     if ('q' in request.GET) and request.GET['q'].strip():
         query_string = request.GET['q']

         entry_query = get_query(query_string, ['episode_name__series_name','episode_name__episode_trailer','custom_description' ]) #'pub_date',])
         #raise Exception(entry_query)

         found_entries = VideoContainer.objects.filter(entry_query).order_by('-pub_date')
         #raise Exception(found_entries)
     return render_to_response('search_page/search_page.html',
                           { 'query_string': query_string, 'found_entries': found_entries },)


