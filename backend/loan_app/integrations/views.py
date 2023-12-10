from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from loan_app.integrations.constants import INTEGRATION_HANDLERS_MAP


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def handle_integration_action(request, name, action):
    if name.lower() not in INTEGRATION_HANDLERS_MAP.keys():
        raise Http404

    handler = INTEGRATION_HANDLERS_MAP[name]()
    action = f'{request.method.lower()}_{action.replace("-", "_")}'
    action_handler = getattr(handler, action, None)

    if not action_handler:
        raise Http404

    data = action_handler()
    return Response(data=data)
