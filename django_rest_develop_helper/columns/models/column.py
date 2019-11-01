from django.db import models

from .column_type import ColumnType

class Column(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        ColumnType,
        related_name='columns',
        on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.name, self.type)

    def str_options(self):
        return ", ".join(str(option) for option in self.options.all())
