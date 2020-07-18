# Generated by Django 3.0.8 on 2020-07-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_date_time',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date_time',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.CharField(default='', max_length=10),
        ),
    ]
