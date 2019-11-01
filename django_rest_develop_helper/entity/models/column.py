from django.db import models
from columns.models.column import Column as ColumnData

from .entity import *

class Column(models.Model):
    data = models.OneToOneField(ColumnData, on_delete=models.CASCADE, primary_key=True)
    entity = models.ForeignKey(Entity, related_name='columns', on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.entity.name, self.data)
