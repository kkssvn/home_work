from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    estimation = models.IntegerField(verbose_name='Оценка')
    group = models.IntegerField(verbose_name='Номер группы')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Список студентов'
        verbose_name_plural = 'Списки студентов'
