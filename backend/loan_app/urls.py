from django.urls import path, include

urlpatterns = [
    path('', include('loan_app.integrations.urls')),
]
