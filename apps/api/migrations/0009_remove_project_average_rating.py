# Generated by Django 3.1.3 on 2020-12-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201130_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='average_rating',
        ),
    ]
