# Generated by Django 2.2.7 on 2020-04-27 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0045_remove_application_jobpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='jobpost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='jobboard.PostJob'),
        ),
    ]
