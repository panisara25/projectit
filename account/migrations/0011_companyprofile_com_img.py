# Generated by Django 2.2.7 on 2020-02-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_companyprofile_com_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='com_img',
            field=models.ImageField(default='userprofile.png', null=True, upload_to='company_img'),
        ),
    ]
