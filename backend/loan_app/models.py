import uuid

from django.db import models

class LoanApplication(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)


class LoanDetails(models.Model):
    loan_application = models.OneToOneField(LoanApplication, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=False, null=False)
    loan_amount = models.PositiveIntegerField(blank=False, null=False)
    balance_sheet = models.JSONField(blank=False, null=False)
    