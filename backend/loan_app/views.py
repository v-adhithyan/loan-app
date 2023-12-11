from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from loan_app.models import LoanApplication, LoanDetails
from loan_app.serializers import LoanDetailsSerializer
from rest_framework.response import Response

from loan_app.integrations.decision_engine.utils import calculate_preassessment_value

from loan_app.integrations.decision_engine.handler import DecisionEngineHandler


@api_view(['POST'])
def initiate_loan_application(request):
    loan_application = LoanApplication.objects.create()
    return JsonResponse({
        'uuid': loan_application.uuid
    })


@api_view(['POST'])
def submit_loan_application(request):
    serializer = LoanDetailsSerializer(data=request.data)
    if serializer.is_valid():
        # Perform additional validations
        validated_data = serializer.validated_data
        established_year = validated_data['established_year']

        try:
            # Get or create a LoanApplication object using the provided uuid
            uuid = validated_data['uuid']
            loan_application, created = LoanApplication.objects.get_or_create(uuid=uuid)

            # Create a LoanDetails object associated with the LoanApplication
            loan_details = LoanDetails(
                loan_application=loan_application,
                business_name=validated_data['business_name'],
                established_year=established_year,
                loan_amount=validated_data['loan_amount'],
                balance_sheet=validated_data['balance_sheet']
            )
            loan_details.save()

            # Calculate pre-assessment before sending to decision engine
            pre_assessment = calculate_preassessment_value(validated_data)
            validated_data.pop('balance_sheet')
            business_details = validated_data
            decision_engine = DecisionEngineHandler(business_details, pre_assessment)
            decision_engine.get_decision()

            return Response(
                {'message': 'LoanDetails created successfully'},
                status=status.HTTP_201_CREATED
            )
        except LoanApplication.DoesNotExist:
            return Response(
                {'error': 'LoanApplication with the provided UUID does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

