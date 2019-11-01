from django.contrib import admin

from .models import *
# Register your models here.

class ColumnOptionInline(admin.StackedInline):
    model = ColumnOption
    extra = 1

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    ordering = ['name', 'type']
    list_display = ('name', 'type', 'options')
    inlines = [ColumnOptionInline]

    def options(self, obj):
        return obj.str_options()

@admin.register(ColumnType)
class ColumnTypeAdmin(admin.ModelAdmin):
    ordering = ['display_name']
    list_display = ('display_name', 'value')

@admin.register(ColumnOption)
class ColumnOptionAdmin(admin.ModelAdmin):
    ordering = ['column']
    list_display = ('column', 'key', 'value')

    def column(self, obj):
        return obj.column.name

@admin.register(ColumnOptionType)
class ColumnOptionTypeAdmin(admin.ModelAdmin):
    ordering = ['display_name']
    list_display = ('display_name', 'value')

@admin.register(ColumnTypeAndOptionTypeRelation)
class ColumnTypeAndOptionTypeRelationAdmin(admin.ModelAdmin):
    ordering = ['column_type', '-required', 'option_type']
    list_display = ('column_type', 'option_type', 'required')
