from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import scrapy
from scrapy.linkextractors import LinkExtractor
import re
from .models import Video

# Create your views here.
class CollectorStart(APIView):
    # name = "rust"
    # allowed_domains = ["www.rust-lang.org"]

    def get(self, response):

        return HttpResponse(status=200)



