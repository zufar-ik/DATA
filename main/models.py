from django.db import models


class News(models.Model):
    title = models.TextField(verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.FileField(verbose_name='Image',upload_to='file/')
