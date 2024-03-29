# Generated by Django 5.0.1 on 2024-02-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegModel',
            fields=[
                ('regid', models.AutoField(primary_key=True, serialize=False)),
                ('Organization_Category', models.CharField(max_length=100)),
                ('Business_Name', models.CharField(max_length=100)),
                ('Address', models.TextField(max_length=100)),
                ('States', models.CharField(max_length=100)),
                ('Cities', models.CharField(max_length=100)),
                ('Pincode', models.IntegerField(null=True)),
                ('Number', models.IntegerField(null=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
