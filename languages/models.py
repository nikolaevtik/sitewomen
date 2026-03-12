from django.db import models
from django.urls import reverse

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ['order']  # сортировка по полю order

    def __str__(self):
        return self.name

def get_absolute_url(self):
    from django.urls import reverse
    return reverse('languages:language_detail', kwargs={'lang_slug': self.slug})
