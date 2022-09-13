from django.contrib import admin

from .models import letter, anniversary

@admin.register(anniversary)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'name', 'date', 'user_id', 'is_active']

@admin.register(letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'user_id', 'anni_id', 'text', 'file', 'is_active']
