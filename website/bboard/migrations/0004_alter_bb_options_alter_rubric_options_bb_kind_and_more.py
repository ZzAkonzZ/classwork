# Generated by Django 4.2.1 on 2023-05-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_rubric'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['name'], 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.AddField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], default='s', max_length=1),
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Загаловок'),
        ),
    ]
