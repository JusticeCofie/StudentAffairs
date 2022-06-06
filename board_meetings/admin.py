from django.contrib import admin
from .models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    list_display = ['description', 'document', 'publish',]

