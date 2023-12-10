import random

from django.urls import reverse
from rest_framework.test import APIRequestFactory

from loan_app.integrations.constants import INTEGRATION_HANDLERS_MAP

from loan_app.integrations.views import handle_integration_action

factory = APIRequestFactory()


def test_configured_integrations():
    integration = 'myob'
    assert integration in INTEGRATION_HANDLERS_MAP
    action = 'balance-sheet'
    kwargs = {
        'name': integration,
        'action': action
    }
    url = reverse('handle-integration-action', kwargs=kwargs)
    request = factory.get(url)
    response = handle_integration_action(request, name=integration, action=action)
    assert response.status_code == 200


def test_non_configured_integrations():
    # Integrations that are not in INTEGRATION_HANDLERS_MAP should throw 404
    integration = random.choice(list(INTEGRATION_HANDLERS_MAP.keys())) + '_'
    assert integration not in INTEGRATION_HANDLERS_MAP
    action = 'balance-sheet'
    kwargs = {
        'name': integration,
        'action': action
    }
    url = reverse('handle-integration-action', kwargs=kwargs)
    request = factory.get(url)
    response = handle_integration_action(request, name=integration, action=action)
    assert response.status_code == 404
