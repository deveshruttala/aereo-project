from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'completed')  # ✅ Shows checkbox in admin list view
    list_filter = ('completed',)
