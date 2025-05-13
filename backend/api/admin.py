"""Файл admin.py."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Класс TaskAdmin."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
