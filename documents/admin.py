from django.contrib import admin
from .models import IncomingDocument, OutgoingDocument


@admin.register(IncomingDocument)
class IncomingDocumentAdmin(admin.ModelAdmin):
    model = IncomingDocument
    list_display = ['sender','subject','received_by']

@admin.register(OutgoingDocument)
class OutgoingDocumentAdmin(admin.ModelAdmin):
    model = IncomingDocument
    list_display = ['destination', 'subject','received_by', 'date_received']