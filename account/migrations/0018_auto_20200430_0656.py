# Generated by Django 3.0.5 on 2020-04-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20200430_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='prove',
            field=models.ImageField(blank=True, null=True, upload_to='prove/'),
        ),
    ]
