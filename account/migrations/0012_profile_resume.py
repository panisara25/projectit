# Generated by Django 3.0.5 on 2020-04-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_companyprofile_com_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='Resume/'),
        ),
    ]
