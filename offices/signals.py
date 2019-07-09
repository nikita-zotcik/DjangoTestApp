from django.db.models.signals import post_save
from django.dispatch import receiver

from offices.models import Company


@receiver(post_save, sender=Company)
def set_headquarter_as_office(sender, instance, **kwargs):
    office = instance.headquarter
    if not office.company:
        office.company = instance
        office.save()
