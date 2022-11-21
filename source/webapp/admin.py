from django.contrib import admin

from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['summary', 'status', 'created_at']
    list_display_links = ['summary']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['task_status']
    list_display_links = ['task_status']
    fields = ['task_status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['task_type']
    list_display_links = ['task_type']
    fields = ['task_type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Type, TypeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
