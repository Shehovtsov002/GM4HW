# Generated by Django 5.0.3 on 2024-04-01 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_chapter_number'),
        ('user_profile', '0003_alter_userprofile_options_alter_userprofile_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile', verbose_name='Author'),
        ),
    ]