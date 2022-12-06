from django.contrib import admin

from webapp.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['summary', 'status', 'project']
    list_display_links = ['summary']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at']
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


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'created_at']
    list_display_links = ['title']
    list_filter = ['start_date']
    search_fields = ['title', 'full_description']
    fields = ['title', 'full_description', 'start_date', 'end_date', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Type, TypeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
