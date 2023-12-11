import json
import uuid

import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from loan_app.models import LoanApplication
from loan_app.views import initiate_loan_application, submit_loan_application
from loan_app.serializers import ESTABLISHED_YEAR_INVALID_MESSAGE
from loan_app.constants import LOAN_APPLICATION_DOES_NOT_EXIST_MESSAGE, LOAN_APPLICATION_SUBMISSION_SUCCESS_MESSAGE

factory = APIRequestFactory()


@pytest.mark.django_db
def test_initiate_loan_application():
    assert LoanApplication.objects.count() == 0

    url = reverse('initiate-loan-application')
    request = factory.post(url)
    response = initiate_loan_application(request)
    response_data = response.data
    assert 'uuid' in response_data
    dataset = LoanApplication.objects.filter(uuid=response_data['uuid'])
    assert len(dataset) == 1
    assert LoanApplication.objects.count() == 1


@pytest.mark.django_db
def test_submit_loan_application(profit_business):
    loan_application = LoanApplication.objects.create()
    balance_sheet = json.dumps(profit_business['balance_sheet'])
    profit_business['balance_sheet'] = balance_sheet

    # Test validation errors

    # Here wrong value for year is passed
    data = profit_business
    data['established_year'] = 20000
    data['uuid'] = loan_application.uuid

    url = reverse('submit-loan-application')
    request = factory.post(url, data=data)
    response = submit_loan_application(request)
    assert response.status_code == 400
    assert 'established_year' in response.data
    assert response.data['established_year'][0] == ESTABLISHED_YEAR_INVALID_MESSAGE

    # Here wrong uuid is passed which does not exist
    _uuid = str(uuid.uuid4())
    data['uuid'] = _uuid
    data['established_year'] = 2000
    with pytest.raises(LoanApplication.DoesNotExist):
        LoanApplication.objects.get(uuid=_uuid)
    request = factory.post(url, data=data)
    response = submit_loan_application(request)
    assert response.status_code == 400
    assert response.data['error'] == LOAN_APPLICATION_DOES_NOT_EXIST_MESSAGE

    # Test happy path
    data['uuid'] = loan_application.uuid
    request = factory.post(url, data=data)
    response = submit_loan_application(request)
    assert response.status_code == 201
    assert response.data['message'] == LOAN_APPLICATION_SUBMISSION_SUCCESS_MESSAGE
