from django.db import models
from django.db.models.fields import CharField

class Task(models.Model):
    title = models.CharField('NAME', max_length=50)
    task = models.TextField('CONTENT')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'