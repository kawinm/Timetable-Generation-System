# Generated by Django 3.0.3 on 2020-02-11 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_dept', models.CharField(max_length=50)),
                ('group_sem', models.IntegerField(default=0)),
                ('group_strength', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=200)),
                ('staff_dept', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=50)),
                ('staff_handling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamgmt.Staff')),
                ('to_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamgmt.Group')),
            ],
        ),
    ]