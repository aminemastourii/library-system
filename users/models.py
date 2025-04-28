from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_borrower=models.BooleanField(default=False)
    def __str__(self):
        return self.username

class BorrowerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birthday=models.DateField()

    def __str__(self):
        return self.user.first_name

    