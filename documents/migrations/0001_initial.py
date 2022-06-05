# Generated by Django 4.0.5 on 2022-06-05 19:05

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
                ('sender', models.CharField(max_length=250, verbose_name='From Who')),
                ('department', models.CharField(choices=[('AFFILIATIONS', 'Head, Affiliations'), ('HEAD', 'Head, Academic and Student Affairs')], max_length=13, verbose_name='Department Been Sent To')),
            ],
            options={
                'verbose_name': 'Incoming Document',
                'verbose_name_plural': 'Incoming Documents',
            },
        ),
        migrations.CreateModel(
            name='OutgoingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject of the Document')),
                ('received_by', models.CharField(max_length=250, verbose_name='Receipent Name')),
                ('date_received', models.DateTimeField()),
                ('department', models.CharField(max_length=250, verbose_name='From Receiving Department')),
                ('destination', models.CharField(max_length=250, verbose_name='Name of Person Sent To')),
            ],
            options={
                'verbose_name': 'Outgoing Document',
                'verbose_name_plural': 'Outgoing Documents',
            },
        ),
    ]
