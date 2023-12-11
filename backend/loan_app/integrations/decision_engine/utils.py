
APPROVAL_RATE_PROFIT_BUSINESS = 60
APPROVAL_RATE_LOSS_BUSINESS = 20
APPROVAL_RATE_BUSINESS_WITH_LARGE_ASSETS = 100

def calculate_preassessment_value(data):
    # assuming the balance sheet only has data for previous year
    # otherwise only 12 entries or entries from previous year needs to be considered

    profit_or_loss = 0
    assets_value = 0

    for bs in data['balance_sheet']:
        profit_or_loss += bs['profitOrLoss']
        assets_value += bs['assetsValue']

    average_assets_value = assets_value / len(data['balance_sheet'])

    if profit_or_loss > 0:
        return APPROVAL_RATE_PROFIT_BUSINESS

    if average_assets_value > data['loan_amount']:
        return APPROVAL_RATE_BUSINESS_WITH_LARGE_ASSETS

    return APPROVAL_RATE_LOSS_BUSINESS
