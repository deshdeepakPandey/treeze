from django.db import models
from .constants import status_options

# Create your models here.

class transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    gross_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0 ,blank=False, null=False)
    status = models.CharField(max_length=20, choices=status_options, default='initiated')
    customer = models.CharField(max_length=200, blank=True, null=True)
    swifter_id = models.CharField(max_length=20, unique=True)
    external_id = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.swifter_id}'
    class Meta:
        ordering = ['-id']

