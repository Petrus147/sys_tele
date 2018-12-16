# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from .models import Executor, Executor2
# from .serializers import ExecutorSerializer
from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import HttpResponse
import pytz

# Create your views here.
class StartExecutor(APIView):
    """
    Start Executor
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        executor = Executor.objects.last()
        executor.start()

        return HttpResponse(status=200)

class StartExecutor2(APIView):
    """
    Start Executor
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        executor = Executor2.objects.last()
        executor.start()

        return HttpResponse(status=200)


# class StopExecutor(APIView):
#     """
#     Stop Executor
#     """
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         executor = Executor.objects.last()
#         executor.stop()
#
#         return HttpResponse(status=200)
#
# class StatusExecutor(APIView):
#     """
#     Status Executor
#     """
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         executor = Executor.objects.last().check_running()
#         # serializer = ExecutorSerializer(executor)
#         context = {
#             'executor': executor,
#         }
#         return Response(context)