# Generated by Django 3.2.6 on 2021-09-08 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventnotice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='post_id',
        ),
    ]