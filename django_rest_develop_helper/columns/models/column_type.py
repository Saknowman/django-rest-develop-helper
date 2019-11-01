from django.db import models

class ColumnType(models.Model):
    display_name = models.CharField(max_length=30, unique=True)
    value = models.CharField(max_length=40, unique=True)
    detail = models.TextField(default='')

    options_type = models.ManyToManyField(
        'columns.ColumnOptionType',
        through='columns.ColumnTypeAndOptionTypeRelation'
    )

    def __str__(self):
        return self.display_name


class ColumnTypeAndOptionTypeRelation(models.Model):
    option_type = models.ForeignKey('columns.ColumnOptionType', on_delete=models.CASCADE)
    column_type = models.ForeignKey(ColumnType, on_delete=models.CASCADE)
    required = models.BooleanField(default=False)
