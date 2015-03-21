from django.contrib import admin
from video_manager.models import *
# Register your models here. E quindi?
# Crea un interfaccia in automatico per gestirli da backend (/admin)
admin.site.register(Series)
admin.site.register(VideoContainer)