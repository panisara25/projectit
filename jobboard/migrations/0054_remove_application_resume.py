# Generated by Django 2.2.7 on 2020-04-28 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0053_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
    ]
