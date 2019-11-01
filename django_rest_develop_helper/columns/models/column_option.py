from django.db import models
from .column import Column

class ColumnOption(models.Model):
    key = models.CharField(max_length=80)
    value = models.CharField(max_length=80)
    column = models.ForeignKey(
        to=Column,
        related_name='options',
        on_delete=models.CASCADE)

    def __str__(self):
        return "{}={}".format(self.key, self.value)


class ColumnOptionType(models.Model):
    display_name = models.CharField(max_length=80, unique=True)
    value = models.CharField(max_length=80, unique=True)
    chioces = models.CharField(max_length=255, null=True)
    detail = models.TextField(default='')

    def __str__(self):
        return self.value
