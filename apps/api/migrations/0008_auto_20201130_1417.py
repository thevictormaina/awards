# Generated by Django 3.1.3 on 2020-11-30 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201130_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='User',
            new_name='user',
        ),
    ]