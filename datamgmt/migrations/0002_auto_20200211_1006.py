# Generated by Django 3.0.3 on 2020-02-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='hours_per_week',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subject',
            name='span',
            field=models.IntegerField(default=1),
        ),
    ]