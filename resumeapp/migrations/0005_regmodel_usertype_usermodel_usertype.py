# Generated by Django 5.0.1 on 2024-02-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_loginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='regmodel',
            name='usertype',
            field=models.CharField(default='company', max_length=100),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='usertype',
            field=models.CharField(default='User', max_length=100),
        ),
    ]