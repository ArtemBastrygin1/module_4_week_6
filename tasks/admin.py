from django.contrib import admin
from .models import Task, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'due_date')
    list_filter = ('owner', 'due_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)

    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'created_at')
    search_fields = ('text',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)
