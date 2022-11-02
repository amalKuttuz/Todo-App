from django.contrib import admin
from.models import TodoModel
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoModel, AuthorAdmin)
