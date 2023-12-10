from loan_app.integrations.accounting_providers.myob import MyobHandler
from loan_app.integrations.accounting_providers.xero import XeroHandler

from loan_app.integrations.decision_engine.handler import DecisionEngineHandler

INTEGRATION_HANDLERS_MAP = {
    'xero': XeroHandler,
    'myob': MyobHandler,
    'decision-engine': DecisionEngineHandler,
}
