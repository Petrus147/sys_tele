# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from video.models import Video, ActiveVideo, ScheduledVideo
# from attendance.models import Attendance
# from employee_hours.models import Employee_hours
from django.db import models
import threading, time
from datetime import datetime, timedelta
import pytz
from django.utils import timezone
# from annoying.functions import get_object_or_None
from time import sleep


# Create your models here.
class Executor(models.Model):
    running = models.BooleanField(default = False)
    interval = models.FloatField(default = 1)
    timestamp = models.DateTimeField(auto_now_add = True, null = True)

    def run_executor(self):
        while self.running:
            print('handle_generators {} delay={}'.format(timezone.now(), (timezone.now() - self.timestamp).total_seconds()))
            self.get_links()
            self.request_link()
            self.timestamp = timezone.now()
            self.save()
            sleep(2)

    def get_links(self):
        scheduled_generators = ScheduledVideo.objects.all()
        for scheduled in scheduled_generators:
            try:
                scheduled.video.get_links()
            except:
                print('{} ERROR:'.format(datetime.now(), scheduled.generator_id))
                return


    def request_link(self):
        active_generators = ActiveVideo.objects.all()
        for active in active_generators:
            try:
                active.video.request_link()
            except:
                print(' ERROR:')
                return

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

