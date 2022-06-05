from django.urls import path
from .views import (
    MeetingListView,
    MeetingCreateView,
    MeetingDetailView,
    MeetingUpdateView,
    MeetingDestroyView
)

app_name ="board_meetings"

urlpatterns = [
    path('create/',MeetingCreateView.as_view()),
    path('list/', MeetingListView.as_view()),
    path('detail/<int:pk>', MeetingDetailView.as_view(),),
    path('update/<int:pk>', MeetingUpdateView.as_view()),
    path('delete/<int:pk>', MeetingDestroyView.as_view(),)
]
