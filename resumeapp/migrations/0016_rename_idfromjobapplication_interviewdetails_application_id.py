# Generated by Django 5.0.1 on 2024-03-09 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0015_interviewdetails_idfromjobapplication_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviewdetails',
            old_name='idFromjobapplication',
            new_name='application_id',
        ),
    ]
