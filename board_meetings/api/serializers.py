from rest_framework import serializers
from board_meetings.models import Meeting

class MeetingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"