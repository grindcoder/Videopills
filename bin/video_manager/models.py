# -*- coding: utf-8 -*-
from django.db import models
import datetime
import time
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Series(models.Model):  # la Serie e i trailer relativi alla serie
    series_name = models.CharField(max_length=50)
    episode_trailer = models.CharField(max_length=50)
    pub_date = models.DateField()


    def __str__(self):
        return " %s Episode: %%s" % self.series_name % self.episode_trailer


class VideoContainer(models.Model):                      # contenitore del video,cioè tutte le info sul video che viene riprodotto
    episode_name = models.ForeignKey(Series)
    episode_trailer_filename = models.FileField(upload_to='pills/%Y/%m/%d', blank=True, null=True)
    ### Modifica per l'aggiunta di video youtube!
    is_youtube_video = models.BooleanField(default=False)  # di default un video non è in formato youtube
    youtube_url = models.CharField(max_length=200, blank=True, null=True)
    ### Fine modifica youtube


    custom_description = models.TextField(max_length=1000, null=True)
    pub_date = models.DateField()


    def __str__(self):
        return "Episose name: %s Custom description: %%s" % self.episode_name %self.custom_description



class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username






