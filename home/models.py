# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid
import datetime
from markdownx.models import MarkdownxField
from django.utils.timezone import now

class post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50)
    content = models.TextField(blank=True)
    md_content = MarkdownxField(default='')
    date = models.DateField(default= now)

    class Meta:
        db_table = 'posts'
        ordering = ['-date']
    def __str__(self):
        return self.slug

class technologies(models.Model):
    item = models.TextField()
    def __str__(self):
        return self.item

class responsibilities(models.Model):
    item = models.TextField()
    def __str__(self):
        return self.item

class project(models.Model):
    name = models.TextField()
    url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(technologies)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.ManyToManyField(responsibilities)
    current = models.BooleanField(blank=True)
    def __str__(self):
        return self.name

class company(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class position(models.Model):
    name = models.TextField()
    company = models.ManyToManyField(company)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.ManyToManyField(responsibilities)
    current = models.BooleanField(blank=True)
    def __str__(self):
        return self.name
