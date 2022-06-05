from rest_framework import generics
from .serializers import OutgoingDocumentSerializer, IncomingDocumentSerializer
from .models import IncomingDocument, OutgoingDocument

class IncomingCreate(generics.CreateAPIView):
    serializer_class = IncomingDocumentSerializer
    
    def get_queryset(self):
        queryset = IncomingDocument.objects.all()
        return queryset
    
    

class IncomingList(generics.ListAPIView):
    serializer_class = IncomingDocumentSerializer
    queryset = IncomingDocument.objects.all()   


class IncomingDetail(generics.RetrieveAPIView):
    serializer_class = IncomingDocumentSerializer
    queryset = IncomingDocument.objects.all()

class IncomingUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = IncomingDocumentSerializer
    queryset = IncomingDocument.objects.all()    

class IncomingDelete(generics.RetrieveDestroyAPIView):
    serializer_class = IncomingDocumentSerializer
    queryset = IncomingDocument.objects.all()
    


class OutgoingCreate(generics.CreateAPIView):
    serializer_class = OutgoingDocumentSerializer
    queryset = OutgoingDocument.objects.all()


class OutgoingList(generics.ListAPIView):
    serializer_class = OutgoingDocumentSerializer
    queryset = OutgoingDocument.objects.all()

class OutgoingDetail(generics.RetrieveAPIView):
    serializer_class = OutgoingDocumentSerializer
    queryset = OutgoingDocument.objects.all()

class OutgoingUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = OutgoingDocumentSerializer
    queryset = OutgoingDocument.objects.all()

class OutgoingDelete(generics.RetrieveDestroyAPIView):
    serializer_class = OutgoingDocumentSerializer
    queryset = OutgoingDocument.objects.all()

