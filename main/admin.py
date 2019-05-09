from django.contrib import admin


# Register your models here.

from django.db import models
from .models import Blog
from tinymce.widgets import TinyMCE

class BlogAdmin(admin.ModelAdmin):
	formfield_overrides = {models.TextField: {'widget': TinyMCE()}}



admin.site.register(Blog, BlogAdmin)
