from django.contrib import admin
from backend.models import Todo


# Register your models here.
class TodoDisplay(admin.ModelAdmin):
    list_display = ['name', 'desc', 'comp']


admin.site.register(Todo, TodoDisplay)