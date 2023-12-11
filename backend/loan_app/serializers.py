from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import LoanDetails

ESTABLISHED_YEAR_INVALID_MESSAGE = 'Established year must be between 1500 and the current year'
class LoanDetailsSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField()

    def validate_established_year(self, value):
        current_year = datetime.now().year
        if value < 1500 or value > current_year:
            raise ValidationError(ESTABLISHED_YEAR_INVALID_MESSAGE)

        return value

    class Meta:
        model = LoanDetails
        fields = ['uuid', 'business_name', 'established_year', 'loan_amount', 'balance_sheet']
