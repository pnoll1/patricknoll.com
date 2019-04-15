# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
import datetime
from markdownx.models import MarkdownxField

class post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    md_content = MarkdownxField()
    date = models.DateField(default=datetime.date.today())

    class Meta:
        db_table = 'posts'
        ordering = ['-date']

class technologies(models.Model):
    item = models.TextField()

class responsibilities(models.Model):
    item = models.TextField()

class project(models.Model):
    name = models.TextField()
    technologies = models.ManyToManyField(technologies)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.ManyToManyField(responsibilities)
