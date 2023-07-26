# Generated by Django 3.2.19 on 2023-07-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_dummymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DummyModel',
        ),
        migrations.AddField(
            model_name='reservation',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='seatStatus',
            field=models.CharField(default='USE', max_length=15),
        ),
    ]
