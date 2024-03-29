# Generated by Django 5.0.3 on 2024-03-21 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_options_remove_book_location_and_more'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_wiki',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата выпуска'),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Inter title')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('number', models.PositiveSmallIntegerField(editable=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
