# Generated by Django 2.2.7 on 2020-02-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0018_postjob_company_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='company_address',
            field=models.TextField(null=True),
        ),
    ]
