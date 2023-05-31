from django.db import models
from django.core import validators

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Bb(models.Model):
    def title_and_price(self):
        # return 'example'
        return f'{self.title} ({self.price})'

    title_and_price.short_description = 'Название и цена'

    KINDS = (('b', "Куплю"),
             ('s', "Продам"),
             ('c', "Обменяю"))
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name="Вид")
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Загаловок', validators=[validators.MinLengthValidator(8, message='Минимум 10 символов')])
    content = models.TextField(null=True, blank=True, verbose_name='Контент')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

