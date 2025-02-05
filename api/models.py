from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_expiry_date(value):
    if value < date.today():
        raise ValidationError("Expiry date cannot be in the past.")

class Policy(models.Model):
    policy_id = models.AutoField(primary_key=True, unique=True)
    customer_name = models.CharField(max_length=255, blank=False, null=False)
    policy_type = models.CharField(max_length=255, blank=False, null=False)
    expiry_date = models.DateField(validators=[validate_expiry_date], blank=False, null=False)
