# Generated by Django 4.0.5 on 2022-06-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=250, verbose_name='Name Of Applicant')),
                ('index', models.CharField(max_length=100, verbose_name='Index Number')),
                ('request_type', models.CharField(choices=[('Letter Of Attestation', 'LETTER OF ATTESTATION'), ('Introductory Letter', 'INTRODUCTORY LETTER'), ('English Proficiency', 'ENGLISH PROFICIENCY'), ('Certification', 'CERTIFICATION'), ('Student Bill', 'STUDENT BILL')], max_length=22, verbose_name='Type Of Request')),
                ('number_of_request', models.PositiveIntegerField(verbose_name='Number Of Request')),
                ('date_of_request', models.DateTimeField(auto_now_add=True, verbose_name='Date Of Request')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact Of Applicant')),
                ('received_by', models.CharField(blank=True, max_length=100, null=True, verbose_name='Received By')),
                ('date_received', models.DateTimeField(blank=True, null=True, verbose_name='Date Received')),
                ('received', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
                'ordering': ['-date_of_request'],
            },
        ),
    ]
