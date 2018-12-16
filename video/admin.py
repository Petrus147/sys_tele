from django.contrib import admin
from .models import Video, AcquiredVideo, ScheduledVideo, RequestedVideo
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('link', 'views', 'category')

class AcquiredVideoAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'video', 'get_link', 'get_views', 'get_category')

    def get_link(self, obj):
        return obj.video.link

    def get_views(self, obj):
        return obj.video.views

    def get_category(self, obj):
        return obj.video.category

    def get_id(self, obj):
        return obj.video.id

class ScheduledVideoAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'video', 'get_link', 'get_views', 'get_category')

    def get_link(self, obj):
        return obj.video.link

    def get_views(self, obj):
        return obj.video.views

    def get_category(self, obj):
        return obj.video.category

    def get_id(self, obj):
        return obj.video.id

class RequestedVideoAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'video', 'get_link', 'get_views', 'get_category')

    def get_link(self, obj):
        return obj.video.link

    def get_views(self, obj):
        return obj.video.views

    def get_category(self, obj):
        return obj.video.category

    def get_id(self, obj):
        return obj.video.id

# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(AcquiredVideo, AcquiredVideoAdmin)
admin.site.register(ScheduledVideo, ScheduledVideoAdmin)
admin.site.register(RequestedVideo, RequestedVideoAdmin)