from loan_app.integrations.handlers import BaseIntegrationHandler


class XeroHandler(BaseIntegrationHandler):
    def get_balance_sheet(self):
        sheet = [
            {
                "year": 2020,
                "month": 12,
                "profitOrLoss": 250000,
                "assetsValue": 1234
            },
            {
                "year": 2020,
                "month": 11,
                "profitOrLoss": 1150,
                "assetsValue": 5789
            },
            {
                "year": 2020,
                "month": 10,
                "profitOrLoss": 2500,
                "assetsValue": 22345
            },
            {
                "year": 2020,
                "month": 9,
                "profitOrLoss": -187000,
                "assetsValue": 223452
            }
        ]
        return sheet