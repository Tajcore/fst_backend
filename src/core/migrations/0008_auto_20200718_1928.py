# Generated by Django 3.0.8 on 2020-07-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200718_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
