# Generated by Django 3.0.5 on 2020-04-29 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20200430_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='file',
        ),
    ]
