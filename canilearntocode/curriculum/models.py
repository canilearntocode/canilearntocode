from django.db import models

from .choices import MEDIUM_CHOICES


class Curriculum(models.Model):
    subject = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    display_order = models.IntegerField(default=1)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Curriculum'

    def __str__(self):
        return self.subject


class Resource(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    creators = models.CharField(max_length=255)
    medium = models.CharField(max_length=3, choices=MEDIUM_CHOICES)
    image = models.ImageField(upload_to='curriculum/')
    subjects = models.ManyToManyField(Curriculum)
    description = models.TextField()

    def __str__(self):
        return self.title

