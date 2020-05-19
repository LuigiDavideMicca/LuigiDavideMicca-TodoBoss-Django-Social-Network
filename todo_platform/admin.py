from django.contrib import admin
from .models import TodoList, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('autore', 'testo', 'creato', TodoList)
    list_filter = ('creato',)
    search_fields = ['autore', 'testo']

admin.site.register(Comment, CommentAdmin)
admin.site.register(TodoList)

