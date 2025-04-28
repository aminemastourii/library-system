from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, BorrowerProfile

@receiver(post_save, sender=User)
def create_borrower_profile(sender, instance, created, **kwargs):
    if created and instance.is_borrower:
        BorrowerProfile.objects.create(user=instance)
