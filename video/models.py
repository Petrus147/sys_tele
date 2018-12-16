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
        # print(self.link)
        html = requests.get(self.link)
        soup = BeautifulSoup(html.content.decode('utf-8', 'ignore'))
        # print(soup.find_all('a'))

        for item in soup.find_all('a'):
            if not item.get('href') is None:
                if "/watch?v=" in item.get('href'):
                    start_link = 'http://www.youtube.com/'
                    if get_object_or_None(Video, link = start_link + item.get('href')) == None:
                        instance = Video.objects.create(link = start_link + item.get('href'))
                        if get_object_or_None(AcquiredVideo, video_id=instance.id) == None:
                            AcquiredVideo.objects.create(video_id=instance.id)

    def request_link(self):
        html = requests.get(self.link)
        # soup = BeautifulSoup(html.content.decode('utf-8', 'ignore'))
        soup = BeautifulSoup(html.content, "html.parser")

        # open('zparsowanyhtml', 'w').write(str(soup))
        # print(soup)
        # print(soup.find_all('a'))
        # for item in soup.find_all('a'):    view-count style-scope yt-view-count-renderer
        try:
            views = soup.find('div', attrs={'class': 'watch-view-count'}).get_text()
            category = soup.find('ul', attrs={'class': 'content watch-info-tag-list'}).get_text()
            import re
            numbers = re.findall(r'\d+', views)
            print(numbers)
            print(len(numbers))
            if len(numbers) == 0:
                return
            else:
                # string = 'xas,xsxs'
                # if ',' in numbers:
                #     instance = Video.objects.get(id = self.id)
                #     ActiveVideo.objects.get(video_id = instance.id).delete()
                #     instance.delete()
                print(numbers)
                views = int(float("".join(numbers)))
                # print(views)
                # print(type(views))
                self.views = views
                self.category = category
                self.save()

        except AttributeError:
            print("ERRORRR")

        # q= textContent.append(name_box)
        # # name = name_box.get_text()
        # views = name_box.find("div").get_text()
        # # for item in soup.find_all('span'):
        #     if not item.get('class') is None:
        #         list(soup.stripped_strings)                # if "/watch?v=" in item.get('class'):
        # from lxml import html
        # import requests
        # page = requests.get(self.link)
        # tree = html.fromstring(page.content)
        # print(tree)
        # views = tree.xpath('//span[@class="stat view-count"]/text()')
        # print(views)



def get_object_or_None(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None


class ScheduledVideo(models.Model):
    video = models.ForeignKey(Video, on_delete = models.SET_NULL, null = True, blank = True)

class AcquiredVideo(models.Model):
    video = models.ForeignKey(Video, on_delete = models.SET_NULL, null = True, blank = True)

class RequestedVideo(models.Model):
    video = models.ForeignKey(Video, on_delete = models.SET_NULL, null = True, blank = True)