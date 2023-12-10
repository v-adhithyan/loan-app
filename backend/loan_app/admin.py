from django.contrib import admin

from loan_app.models import LoanDetails, LoanApplication

# Register your models here.
class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'established_year', 'loan_amount', )

admin.site.register(LoanApplication)
admin.site.register(LoanDetails, LoanDetailsAdmin)
