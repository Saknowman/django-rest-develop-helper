from django.dispatch import receiver
from django.db.models.signals import post_delete

from ..models import Column

@receiver(post_delete, sender=Column)
def delete_related_column_data(sender, **kwargs):
    deleted_column = kwargs['instance']
    deleted_column.data.delete()
