from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=250)
    task = models.TextField('Описание')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title