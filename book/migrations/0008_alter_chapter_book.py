# Generated by Django 5.0.3 on 2024-04-03 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='book.book'),
        ),
    ]
