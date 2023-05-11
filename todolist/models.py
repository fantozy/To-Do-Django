from django.db import models


class ToDo(models.Model):
    title =  models.CharField('Task name', max_length=500)
    is_complete = models.BooleanField('Complete', default=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    def __str__(self):
        return self.title
    



