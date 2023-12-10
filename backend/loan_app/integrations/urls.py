from django.urls import path

from loan_app.integrations.views import handle_integration_action

urlpatterns = [
    path('integration/<str:name>/<str:action>/', handle_integration_action, name='handle-integration-action'),
]
