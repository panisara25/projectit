# Generated by Django 2.2.7 on 2020-04-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0061_auto_20200428_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='Resume_file/'),
        ),
    ]
