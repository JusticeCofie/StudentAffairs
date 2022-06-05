from django.db import models

class Request(models.Model):
    TYPE_OF_REQUEST =(
        ('Letter Of Attestation', 'LETTER OF ATTESTATION'),
        ('Introductory Letter', 'INTRODUCTORY LETTER'),
        ('English Proficiency', 'ENGLISH PROFICIENCY'),
        ('Certification', 'CERTIFICATION'),
        ('Student Bill','STUDENT BILL'),
    )
    applicant = models.CharField(max_length=250, verbose_name='Name Of Applicant')
    index = models.CharField(max_length=100, verbose_name='Index Number')
    request_type = models.CharField(choices=TYPE_OF_REQUEST, verbose_name='Type Of Request', max_length=22)
    number_of_request = models.PositiveIntegerField(verbose_name='Number Of Request')
    date_of_request = models.DateTimeField(auto_now_add=True, verbose_name='Date Of Request')
    contact = models.CharField(max_length=15, verbose_name='Contact Of Applicant')
    received_by = models.CharField(max_length=100, verbose_name='Received By', blank=True, null=True)
    date_received = models.DateTimeField(verbose_name='Date Received', blank=True, null=True)
    received = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['-date_of_request',]
    
    def __str__(self):
        return f"{self.applicant}"
    