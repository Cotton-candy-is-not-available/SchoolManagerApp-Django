# Generated by Django 5.1.3 on 2025-02-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='[Event Name]', max_length=100)),
                ('date_of_event', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
