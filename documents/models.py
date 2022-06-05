from django.db import models

class Record(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Subject of the Document')
    received_by = models.CharField(max_length=250, verbose_name='Receipent Name')
    date_received = models.DateTimeField()
    department = models.CharField(max_length=250, verbose_name='From Receiving Department')
    
    class Meta:
        abstract = True
        ordering = ['-date_received',]

class IncomingDocument(Record):
    DEPARTMENT = (
        ('AFFILIATIONS','Head, Affiliations'),
        ('HEAD', 'Head, Academic and Student Affairs'),
    )
    sender = models.CharField(max_length=250, verbose_name='From Who')
    department = models.CharField(choices=DEPARTMENT, max_length=13, verbose_name='Department Been Sent To')

    class Meta:
        verbose_name = 'Incoming Document'
        verbose_name_plural = 'Incoming Documents'


class OutgoingDocument(Record):
    destination = models.CharField(max_length=250, verbose_name='Name of Person Sent To')
    
    class Meta:
        verbose_name ='Outgoing Document'
        verbose_name_plural = 'Outgoing Documents'