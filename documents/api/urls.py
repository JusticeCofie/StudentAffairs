from django.urls import path
from .views import ( 
    IncomingDelete, IncomingList,
    IncomingCreate, IncomingUpdate, 
    IncomingDetail, OutgoingCreate, 
    OutgoingDelete, OutgoingList, 
    OutgoingDetail, OutgoingUpdate
    )

app_name = 'documents'

urlpatterns = [
    path('', IncomingList.as_view()),
    path('incoming/create/', IncomingCreate.as_view()),
    path('incoming/<int:pk>/', IncomingDetail.as_view()),
    path('incoming/update/<int:pk>/', IncomingUpdate.as_view()),
    path('incoming/delete/<int:pk>/', IncomingDelete.as_view()),

    path('outgoing/', OutgoingList.as_view()),
    path('outgoing/create/', OutgoingCreate.as_view()),
    path('outgoing/<int:pk>/',OutgoingDetail.as_view()),
    path('outgoing/update/<int:pk>/',OutgoingUpdate.as_view()),
    path('outgoing/delete/<int:pk>/',OutgoingDelete.as_view()),

]
