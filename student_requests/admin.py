from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestModelAdmin(admin.ModelAdmin):
    model = Request
    list_display = ['applicant', 'index', 'request_type','date_of_request']
