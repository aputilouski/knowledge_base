from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':40, 'cols':180})},
    }
    list_display = ('title', 'category', 'weight')
    list_filter = ['category']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
