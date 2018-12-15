from django.contrib import admin
from .models import Video, ActiveVideo, ScheduledVideo
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('link', 'views', 'category')

class ActiveVideoAdmin(admin.ModelAdmin):
    list_display = ('video',)

class ScheduledVideoAdmin(admin.ModelAdmin):
    list_display = ('video',)
# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(ActiveVideo, ActiveVideoAdmin)
admin.site.register(ScheduledVideo, ScheduledVideoAdmin)