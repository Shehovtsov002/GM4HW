from django.db import models


# Create your models here.
class Book(models.Model):
    LOCALIZATION_CHOICES = (
        ('Английский', 'Английский'),
        ('Кыргызский', 'Кыргызский'),
        ('Русский', 'Русский')
    )
    title = models.CharField(null=True, max_length=50, verbose_name="Название книги")
    author = models.CharField(null=True, max_length=50, verbose_name="Автор")
    author_wiki = models.URLField(null=True, blank=True, verbose_name="Ссылка на вики автора")
    description = models.TextField(null=True, verbose_name="Описание книги")
    cover = models.ImageField(upload_to='images/', verbose_name="Загрузите обложку книги", null=True)
    audio = models.FileField(upload_to='audio/', verbose_name="Загрузите аудиокнигу", null=True)
    age_restriction = models.PositiveSmallIntegerField(default=0, verbose_name="Возрастное ограничение от")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Укажите цену", default=100)
    localization = models.CharField(null=True, max_length=25, choices=LOCALIZATION_CHOICES, verbose_name="Язык книги")
    created_at = models.DateField(null=True, verbose_name="Дата выпуска")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
