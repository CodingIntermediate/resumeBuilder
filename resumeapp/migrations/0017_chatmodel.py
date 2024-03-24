# Generated by Django 5.0.1 on 2024-03-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0016_rename_idfromjobapplication_interviewdetails_application_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
