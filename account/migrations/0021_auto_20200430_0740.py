# Generated by Django 3.0.5 on 2020-04-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20200430_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default='1.docx', null=True, upload_to='Resume/'),
        ),
    ]
