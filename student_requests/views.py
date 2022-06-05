from django.http import Http404
from rest_framework import generics
from .models import Request
from .serializers import RequestSerializers


class RequestCreateView(generics.CreateAPIView):
    serializer_class = RequestSerializers
    queryset = Request.objects.all()


class RequestList(generics.ListAPIView):
    serializer_class = RequestSerializers
    queryset = Request.objects.all()


class RequestDetail(generics.RetrieveAPIView):
    serializer_class = RequestSerializers
    queryset = Request.objects.all()


class RequestUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = RequestSerializers
    queryset = Request.objects.all()


class RequestDeleteView(generics.DestroyAPIView):
    serializer_class = RequestSerializers
    queryset = Request.objects.all()
    