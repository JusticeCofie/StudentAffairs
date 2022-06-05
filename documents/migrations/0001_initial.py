# Generated by Django 4.0.4 on 2022-06-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject of the Document')),
                ('received_by', models.CharField(max_length=250, verbose_name='Receipent Name')),
                ('date_received', models.DateTimeField()),
                ('department', models.CharField(max_length=250, verbose_name='Department')),
                ('sent_by', models.CharField(max_length=250, verbose_name='From Who')),
            ],
            options={
                'verbose_name': 'IncomingDocument',
                'verbose_name_plural': 'IncomingDocuments',
            },
        ),
        migrations.CreateModel(
            name='OutgoingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject of the Document')),
                ('received_by', models.CharField(max_length=250, verbose_name='Receipent Name')),
                ('date_received', models.DateTimeField()),
                ('department', models.CharField(max_length=250, verbose_name='Department')),
                ('destination', models.CharField(max_length=250, verbose_name='Name of Person Sent To')),
            ],
            options={
                'verbose_name': 'OutgoingDocument',
                'verbose_name_plural': 'OutgoingDocuments',
            },
        ),
    ]
