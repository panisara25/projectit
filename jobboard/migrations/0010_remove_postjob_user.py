# Generated by Django 2.2.7 on 2020-02-18 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0009_postjob_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='user',
        ),
    ]
