from datetime import datetime

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


class Films(models.Model):
    category = models.ManyToManyField('Category', verbose_name="Category", null=True, blank=True)
    name = models.CharField(max_length=255)
    date_made = models.DateTimeField(default=datetime.now, blank=True)
    acteru = models.TextField()
    date_show = models.DateField()