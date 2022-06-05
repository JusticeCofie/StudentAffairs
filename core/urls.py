
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('documents.api.urls', namespace='documents')),
    path('request/', include('student_requests.api.urls')),
    path('board/',include('board_meetings.api.urls',)),
]
