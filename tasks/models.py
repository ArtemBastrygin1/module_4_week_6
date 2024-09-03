from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
NULLABLE = {
    'blank': True,
    'null': True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    color = models.CharField(max_length=20, verbose_name='Цвет категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'tags'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(**NULLABLE, verbose_name='Описание задачи')
    due_date = models.DateTimeField(**NULLABLE, verbose_name='Сроки выполнения')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='tasks', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', verbose_name='Категория')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        db_table = 'tasks'

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name='Задача')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'

    def __str__(self):
        return self.comment


