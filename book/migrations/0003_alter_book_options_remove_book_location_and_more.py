# Generated by Django 5.0.3 on 2024-03-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.AddField(
            model_name='book',
            name='age_restriction',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Возрастное ограничение от'),
        ),
        migrations.AddField(
            model_name='book',
            name='audio',
            field=models.FileField(null=True, upload_to='audio/', verbose_name='Загрузите аудиокнигу'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='book',
            name='author_wiki',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на вики автора'),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Загрузите обложку книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='localization',
            field=models.CharField(choices=[('Английский', 'Английский'), ('Кыргызский', 'Кыргызский'), ('Русский', 'Русский')], max_length=25, null=True, verbose_name='Язык книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(null=True, verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10, verbose_name='Укажите цену'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Название книги'),
        ),
    ]
