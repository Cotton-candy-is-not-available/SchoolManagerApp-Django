# Generated by Django 5.1.3 on 2025-02-17 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='td_list',
            old_name='name',
            new_name='List_name',
        ),
    ]
