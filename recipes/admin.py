from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at')
    list_editable = ('is_published',)


admin.site.register(Category, CategoryAdmin)
