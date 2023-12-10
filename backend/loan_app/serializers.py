from rest_framework import serializers
from .models import LoanDetails

class LoanDetailsSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField()
    class Meta:
        model = LoanDetails
        fields = ['uuid', 'business_name', 'established_year', 'loan_amount', 'balance_sheet']
