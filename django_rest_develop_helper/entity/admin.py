from django.contrib import admin

from .models import *
from columns.admin import Column as ColumnData
# Register your models here.

class ColumnInline(admin.StackedInline):
    model = Column
    extra = 1


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'columns')
    inlines = [ColumnInline]

    def columns(self, obj):
        return ", ".join(str(column) for column in obj.columns.all())


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    ordering = ['entity', 'data']
    list_display = ('entity', 'data')
