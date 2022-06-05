from rest_framework import serializers
from student_requests.models import Request

class RequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('__all__')