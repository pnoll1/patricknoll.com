# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import post, technologies, responsibilities, project, position, company
from markdownx.admin import MarkdownxModelAdmin

myModels = [technologies, responsibilities, project, position, company]
admin.site.register(myModels)
#register models that need markdown
admin.site.register(post,MarkdownxModelAdmin)
