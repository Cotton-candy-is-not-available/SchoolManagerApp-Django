# Generated by Django 5.1.3 on 2025-02-14 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManager', '0002_event_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='test',
        ),
    ]
