from rest_framework import generics
from .serializers import MeetingSerializers
from board_meetings.models import Meeting 

class MeetingCreateView(generics.CreateAPIView):
    serializer_class = MeetingSerializers
    queryset = Meeting.objects.all()

class MeetingListView(generics.ListAPIView):
    serializer_class = MeetingSerializers
    queryset = Meeting.objects.all()

class MeetingDetailView(generics.RetrieveAPIView):
    serializer_class = MeetingSerializers
    queryset = Meeting.objects.all()

class MeetingUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = MeetingSerializers
    queryset = Meeting.objects.all()

class MeetingDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = MeetingSerializers
    queryset = Meeting.objects.all()

