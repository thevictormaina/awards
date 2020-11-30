# Generated by Django 3.1.3 on 2020-11-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201130_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='design',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='usability',
            field=models.IntegerField(null=True),
        ),
    ]