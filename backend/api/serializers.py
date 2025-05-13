"""Файл serializers.py."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор."""

    class Meta:
        """Класс Meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
