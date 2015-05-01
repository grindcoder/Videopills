# -*- coding: utf-8 -*-
import datetime
from video_manager.models import VideoContainer
from django.shortcuts import render_to_response
import re
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from video_manager.forms import  UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from post_office import mail
from core import settings

# Create your views here.

@login_required(login_url="/login")
def home(request):
    # TODO gabri
    # Non prendere tutti i video pills ma solo gli ultimi 6 che sono stati inseriti
    # in ordine temporale
    pills= VideoContainer.objects.all().order_by('-pub_date')[:4]

    return render_to_response('home/home.html', {"list_of_pills":pills},
                              context_instance=RequestContext(request))

def redirect_to_videopills():
    return "fuck"

def test_mail(request):

    mail.send(
        ['ursinogabriele.0@gmail.com','chiora93@gmail.com'], # List of email addresses also accepted
        'noreply@blozzer.it',
        subject='My email',
        message='Hi there!',
        html_message='Hi <strong>there</strong>!',
    )

    return HttpResponse("SENT")

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



@login_required(login_url="/login")
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
                              { 'query_string': query_string, 'found_entries': found_entries , 'no_header' : True} ,
                            context_instance=RequestContext(request))




def register(request):

    registered = False
    errors = None


    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() :#and profile_form.is_valid():
        # Save the user's form data to the database.

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #profile = profile_form.save()
            #profile.user = user

            #profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True


        ## INVIO MAIL
        ## La invio prima all'utente

        mail.send(
            [user.email],
            'noreply@blozzer.it',
            template='thankyou_registration',
            render_on_delivery=True,
            context={'username': request.POST.get('username', '')},
        )

        ## Invio agli amministratori per notificare l'iscrizione al sito
        for administrator in settings.ADMINS:
            mail.send(
                [administrator[1]],
                'noreply@blozzer.it',
                template='thankyou_registration_backend',
                render_on_delivery=True,

                context={'administrator_name': administrator[0], 'username': user.username},
            )

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            errors = user_form.errors


    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()


    # Render the template depending on the context.
    return render(request,
            'Authentication/register_page.html',
            {'user_form': user_form,  'registered': registered, 'errors' : errors} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        errors = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                # An inactive account was used - no logging in!
                return render_to_response('Authentication/register_page.html', {'form': form},
                                          context_instance=RequestContext(request))

        else:
             # Bad login details were provided. So we can't log the user in.
             # Redirect to register page
             errors['message'] = "Credenziali non valide"
             # No context variables to pass to the template system, hence the
             # blank dictionary object...
             return render(request, 'Authentication/login_page.html', {'errors' : errors, 'no_header': True})


    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'Authentication/login_page.html', {'no_header' : True})


