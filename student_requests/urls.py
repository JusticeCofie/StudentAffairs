from django.urls import path
from .views import RequestList, RequestDetail, RequestCreateView, RequestUpdateView, RequestDeleteView

app_name = 'student_requets'

urlpatterns = [
    path('create/', RequestCreateView.as_view()),
    path('list/',RequestList.as_view()),
    path('detail/<int:pk>/', RequestDetail.as_view()),
    path('update/<int:pk>/', RequestUpdateView.as_view()),
    path('delete/<int:pk>/', RequestDeleteView.as_view()),
]
