# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from video.models import Video, AcquiredVideo, ScheduledVideo, RequestedVideo
# from attendance.models import Attendance
# from employee_hours.models import Employee_hours
from django.db import models
import threading, time
from datetime import datetime, timedelta
import pytz
from django.utils import timezone
# from annoying.functions import get_object_or_None
from time import sleep
from video.models import get_object_or_None

# Create your models here.
class Executor(models.Model):
    running = models.BooleanField(default = False)
    interval = models.FloatField(default = 1)
    timestamp = models.DateTimeField(auto_now_add = True, null = True)

    def run_executor(self):
        while self.running:
            print('1 {} delay={}'.format(timezone.now(), (timezone.now() - self.timestamp).total_seconds()))
            self.get_links()
            # self.request_link()
            self.timestamp = timezone.now()
            self.save()
            sleep(1)

    def get_links(self):
        acquired_videos = AcquiredVideo.objects.all()
        for acquired in acquired_videos:
            # print(scheduled.video.link)
            # try:
            acquired.video.get_links()
            # except:
            #     print('ERROR:')
            #     return
            if get_object_or_None(AcquiredVideo, video_id = acquired.video.id) != None:
                AcquiredVideo.objects.get(video_id = acquired.video.id).delete()
                if get_object_or_None(ScheduledVideo, video_id = acquired.video.id) == None:
                    ScheduledVideo.objects.create(video_id = acquired.video.id)

    # def request_link(self):
    #     active_videos = ActiveVideo.objects.all()
    #     for active in active_videos:
    #         # print(active.video.link)
    #         active.video.request_link()

    def start(self):

        if not self.check_running().running:
            self.running = True
            self.timestamp = timezone.now()
            self.save()
            print('{} executor={} START'.format(datetime.now(), self.id))
            threading.Timer(0, self.run_executor).start()
        else:
            print('{} executor={} ALREADY RUNNING'.format(datetime.now(), self.id))
    #
    #
    # def stop(self):
    #     self.running = False
    #     self.save()
    #     print('{} executor={} STOP'.format(datetime.now(), self.id))
    #
    def check_running(self):
        delay = datetime.utcnow().replace(tzinfo=pytz.UTC) - self.timestamp.replace(tzinfo=pytz.UTC)
        interval = timedelta(0, 0, 0, self.interval*1000)
        self.running = delay <= interval
        self.save()
        return self




class Executor2(models.Model):
    running = models.BooleanField(default = False)
    interval = models.FloatField(default = 1)
    timestamp = models.DateTimeField(auto_now_add = True, null = True)

    def run_executor(self):
        while self.running:
            print('2 {} delay={}'.format(timezone.now(), (timezone.now() - self.timestamp).total_seconds()))
            # self.get_links()
            self.request_link()
            self.timestamp = timezone.now()
            self.save()
            sleep(1)

    # def get_links(self):
    #     scheduled_videos = ScheduledVideo.objects.all()
    #     for scheduled in scheduled_videos:
    #         # print(scheduled.video.link)
    #         # try:
    #         scheduled.video.get_links()
    #         # except:
    #         #     print('ERROR:')
    #         #     return
    #         if get_object_or_None(ScheduledVideo, video_id = scheduled.video.id) != None:
    #             ScheduledVideo.objects.get(video_id = scheduled.video.id).delete()
    #             if get_object_or_None(ActiveVideo, video_id = scheduled.video.id) == None:
    #                 ActiveVideo.objects.create(video_id = scheduled.video.id)

    def request_link(self):
        scheduled_videos = ScheduledVideo.objects.all()
        for scheduled in scheduled_videos:
            try:
                # print(active.video.link)
                scheduled.video.request_link()

                if get_object_or_None(ScheduledVideo, video_id=scheduled.video.id) != None:
                    ScheduledVideo.objects.get(video_id=scheduled.video.id).delete()
                    if get_object_or_None(RequestedVideo, video_id=scheduled.video.id) == None:
                        RequestedVideo.objects.create(video_id=scheduled.video.id)
            except AttributeError:
                print("ERRORRR")

    def start(self):

        if not self.check_running().running:
            self.running = True
            self.timestamp = timezone.now()
            self.save()
            print('{} executor={} START'.format(datetime.now(), self.id))
            threading.Timer(0, self.run_executor).start()
        else:
            print('{} executor={} ALREADY RUNNING'.format(datetime.now(), self.id))
    #
    #
    # def stop(self):
    #     self.running = False
    #     self.save()
    #     print('{} executor={} STOP'.format(datetime.now(), self.id))
    #
    def check_running(self):
        delay = datetime.utcnow().replace(tzinfo=pytz.UTC) - self.timestamp.replace(tzinfo=pytz.UTC)
        interval = timedelta(0, 0, 0, self.interval*1000)
        self.running = delay <= interval
        self.save()
        return self