from django.db import models
from bs4 import BeautifulSoup
import requests
from django.shortcuts import _get_queryset

# Create your models here.
class Video(models.Model):
    link = models.URLField(max_length=200, blank=True, null=True)
    views = models.BigIntegerField(default=0)
    category = models.CharField(max_length=64, blank=True, null=True)

    def get_links(self):

        if self.link == None:
            self.link = 'http://www.youtube.com/'
            print('save but its no obj')
        html = requests.get(self.link)
        soup = BeautifulSoup(html.content.decode('utf-8', 'ignore'))
        # print(soup.find_all('a'))
        for item in soup.find_all('a'):
            if not item.get('href') is None:
                if "/watch?v=" in item.get('href'):
                    if self.get_object_or_None(Video, link= item.get('href')) != None:
                        instance = Video.objects.get(link = item.get('href'))
                        if self.get_object_or_None(ScheduledVideo, video_id=instance.id) != None:
                            ScheduledVideo.objects.get(video_id=instance.id).delete()
                            if self.get_object_or_None(ActiveVideo, video_id=instance.id) == None:
                                ActiveVideo.objects.create(video_id=instance.id)
                        print(instance)
                    else:
                        instance = Video.objects.create(link = item.get('href'))
                        if self.get_object_or_None(ScheduledVideo, video_id=instance.id) == None:
                            ScheduledVideo.objects.create(video_id=instance.id)

    # def request_link(self):
    #     # html = requests.get(self.link)
    #     # soup = BeautifulSoup(html.content.decode('utf-8', 'ignore'))
    #     # # print(soup.find_all('a'))
    #     # for item in soup.find_all('a'):

    def get_object_or_None(klass, *args, **kwargs):
        queryset = _get_queryset(klass)
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            return None


class ActiveVideo(models.Model):
    video = models.ForeignKey(Video, on_delete = models.SET_NULL, null = True, blank = True)

class ScheduledVideo(models.Model):
    video = models.ForeignKey(Video, on_delete = models.SET_NULL, null = True, blank = True)

