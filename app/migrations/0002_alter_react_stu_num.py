# Generated by Django 3.2.19 on 2023-05-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='stu_num',
            field=models.CharField(max_length=20),
        ),
    ]
