from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "{}".format(self.name)
