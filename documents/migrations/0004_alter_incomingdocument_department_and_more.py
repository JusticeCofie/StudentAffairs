# Generated by Django 4.0.4 on 2022-06-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_rename_sent_by_incomingdocument_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingdocument',
            name='department',
            field=models.CharField(choices=[('AFFILIATIONS', 'Head, Affiliations'), ('HEAD', 'Head, Academic and Student Affairs')], max_length=13, verbose_name='Department Been Sent To'),
        ),
        migrations.AlterField(
            model_name='outgoingdocument',
            name='department',
            field=models.CharField(max_length=250, verbose_name='From Receiving Department'),
        ),
    ]