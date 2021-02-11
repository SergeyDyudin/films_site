from django.db import models


class Records(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    date = models.DateField(verbose_name='Дата')
    video = models.FileField(verbose_name='Видео', upload_to='records/video/')
    description = models.TextField(verbose_name='Описание', max_length=500, blank=True)


    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.name