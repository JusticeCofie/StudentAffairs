from django.urls import path
from .views import HomePageView, meeting_list, upload_document

app_name = 'academic_meetings'

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('meeting/', meeting_list, name='meeting-list'),
    path('upload/',upload_document, name='upload'),
]