from django.db import models
from user_profile.models import UserProfile


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'#{self.name}'


class Book(models.Model):
    LOCALIZATION_CHOICES = (
        ('Английский', 'Английский'),
        ('Кыргызский', 'Кыргызский'),
        ('Русский', 'Русский')
    )
    title = models.CharField(null=True, max_length=50, verbose_name="Название книги")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Author", null=False, default=1)
    description = models.TextField(null=True, verbose_name="Описание книги")
    cover = models.ImageField(upload_to='images/', verbose_name="Загрузите обложку книги", null=True)
    age_restriction = models.PositiveSmallIntegerField(default=0, verbose_name="Возрастное ограничение от")
    localization = models.CharField(null=True, max_length=25, choices=LOCALIZATION_CHOICES, verbose_name="Язык книги")
    created_at = models.DateField(null=True, verbose_name="Дата выпуска", auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name="Жанры книги", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=50, verbose_name="Inter title")
    text = models.TextField(verbose_name="Text", null=True)
    created_at = models.DateField(auto_now_add=True)
    number = models.PositiveSmallIntegerField(editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.number:
            last_chapter = Chapter.objects.filter(book=self.book).order_by('-number').first()
            if last_chapter:
                self.number = last_chapter.number + 1
            else:
                self.number = 1
        super().save(*args, **kwargs)
