# Generated by Django 5.0.1 on 2024-03-24 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0018_alter_chatmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='resumeapp.usermodel'),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='resumeapp.usermodel'),
        ),
    ]