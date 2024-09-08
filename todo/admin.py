from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','tag','updated_at')
    search_fields = ('task','tag')


admin.site.register(Task, TaskAdmin)