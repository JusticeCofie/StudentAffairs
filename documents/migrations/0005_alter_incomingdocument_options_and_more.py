# Generated by Django 4.0.4 on 2022-06-01 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_incomingdocument_department_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomingdocument',
            options={'verbose_name': 'Incoming Document', 'verbose_name_plural': 'Incoming Documents'},
        ),
        migrations.AlterModelOptions(
            name='outgoingdocument',
            options={'verbose_name': 'Outgoing Document', 'verbose_name_plural': 'Outgoing Documents'},
        ),
    ]
