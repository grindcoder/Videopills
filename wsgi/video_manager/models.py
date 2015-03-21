from django.db import models



# Create your models here.
class Series(models.Model):  # la Serie e i trailer relativi alla serie
    series_name = models.CharField(max_length=50)
    episode_trailer = models.CharField(max_length=50)

    def __str__(self):
        return "Name: %s Episode: %%s" % self.series_name % self.episode_trailer


class VideoContainer (models.Model):                      # contenitore del video,cioè tutte le info sul video che viene riprodotto
    episode_name = models.ForeignKey(Series)
    episode_trailer_filename = models.CharField(max_length= 100)
    custom_description = models.TextField(max_length=1000, null=True)


