from django.urls import path, include

from .views import initiate_loan_application, submit_loan_application

urlpatterns = [
    path('', include('loan_app.integrations.urls')),
    path('loan-application/initiate/', initiate_loan_application, name='initiate-loan-application'),
    path('loan-application/submit/', submit_loan_application, name='submit-loan-application'),
]
