from loan_app.integrations.handlers import BaseIntegrationHandler


class DecisionEngineHandler(BaseIntegrationHandler):

    def __init__(self, business_details, pre_assessment):
        self.business_details = business_details
        self.pre_assessment = pre_assessment

    def get_decision(self):
        return {}
