# Generated by Django 5.0.1 on 2024-03-09 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0014_interviewdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewdetails',
            name='idFromjobapplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resumeapp.jobapplication'),
        ),
        migrations.AlterField(
            model_name='interviewdetails',
            name='interviewDetails',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
