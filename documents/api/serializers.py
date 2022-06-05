from rest_framework import serializers
from documents.models import IncomingDocument, OutgoingDocument

class IncomingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingDocument
        fields = ('__all__')
    
class OutgoingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingDocument
        fields = ('__all__')