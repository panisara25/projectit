# Generated by Django 2.2.7 on 2020-04-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0038_application'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-date_applied', '-updated']},
        ),
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
    ]
