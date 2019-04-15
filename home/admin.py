# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(post,MarkdownxModelAdmin)
