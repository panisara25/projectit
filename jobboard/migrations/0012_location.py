# Generated by Django 2.2.7 on 2020-02-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0011_postjob_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
