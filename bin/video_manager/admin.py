# -*- coding: utf-8 -*-

from django.contrib import admin
from video_manager.models import *
from video_manager.models import UserProfile


# Register your models here. E quindi?
# Crea un interfaccia in automatico per gestirli da backend (/admin)
admin.site.register(Series)
admin.site.register(VideoContainer)
admin.site.register(UserProfile)