# Generated by Django 5.1 on 2024-08-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='github_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='linkedin_url',
            field=models.URLField(blank=True),
        ),
    ]
