# Generated by Django 3.0.5 on 2020-04-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20200430_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default='userprofile.png', null=True, upload_to='Resume/'),
        ),
    ]
