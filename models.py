from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50)
    UID = models.CharField(primary_key='True', max_length=15)
    # email = models.EmailField(blank='False')
    # pwd = models.CharField(max_length=100)
    # idProof = models.ImageField(upload_to='Logos/Client_ID')
   # DOB = models.DateField()
    address = models.TextField(null='True')
    available_bal = models.PositiveIntegerField(default=0)
    invested_bal = models.PositiveIntegerField(default=0)
    demat_ac = models.IntegerField()
    bank_ac = models.IntegerField()
    gender_choices = [('M', "Male"), ('F', 'Female'), ('O', 'Prefer not to say')]
    gender = models.CharField(max_length=1, choices=gender_choices, default='M')

    def __str__(self):
        return str(self.user)

    def save(self):
        super().save()



