# Generated by Django 3.0.5 on 2020-04-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20200430_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='prove',
            field=models.ImageField(blank=True, default='userprofile.png', null=True, upload_to='prove/'),
        ),
    ]
