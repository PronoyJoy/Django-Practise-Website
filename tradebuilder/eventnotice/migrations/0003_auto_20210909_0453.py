# Generated by Django 3.2.6 on 2021-09-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventnotice', '0002_remove_event_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creation',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='numberofpeople',
            field=models.IntegerField(null=True),
        ),
    ]
