from rest_framework import  serializers

from loan_app.models import LoanApplication


class LoanApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoanApplication
        fields = '__all__'
