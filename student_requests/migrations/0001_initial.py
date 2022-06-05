# Generated by Django 4.0.4 on 2022-06-01 15:19

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
                ('number_of_request', models.IntegerField(verbose_name='Number Of Request')),
                ('date_of_request', models.DateTimeField(auto_now_add=True, verbose_name='Date Of Request')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact Of Applicant')),
                ('received_by', models.CharField(max_length=100, verbose_name='Received By')),
                ('date_received', models.DateTimeField(verbose_name='Date Received')),
                ('received', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Request',
            },
        ),
    ]
