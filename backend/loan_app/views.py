from django.http import JsonResponse
from rest_framework.decorators import api_view

from loan_app.models import LoanApplication

@api_view(['POST'])
def initiate_loan_application(request):
    loan_application = LoanApplication.objects.create()
    return JsonResponse({
        'uuid': loan_application.uuid
    })


@api_view(['POST'])
def submit_loan_application(request):
    return JsonResponse({
        'message': 'Loan request received.'
    })
