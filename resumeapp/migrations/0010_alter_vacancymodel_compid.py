# Generated by Django 5.0.1 on 2024-02-24 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0009_alter_vacancymodel_compid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancymodel',
            name='compid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resumeapp.regmodel'),
        ),
    ]
