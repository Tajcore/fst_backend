# Generated by Django 3.0.8 on 2020-07-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200719_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
