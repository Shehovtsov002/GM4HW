# Generated by Django 5.0.3 on 2024-03-28 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0002_bazarparser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bazarparser',
            name='image',
        ),
    ]
