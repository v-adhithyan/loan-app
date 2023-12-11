from loan_app.integrations.decision_engine.utils import (calculate_preassessment_value, APPROVAL_RATE_PROFIT_BUSINESS,
                                                         APPROVAL_RATE_LOSS_BUSINESS,
                                                         APPROVAL_RATE_BUSINESS_WITH_LARGE_ASSETS)


def test_calculate_pre_assessment_value_for_profit_business(profit_business):
    value = calculate_preassessment_value(profit_business)
    assert value == APPROVAL_RATE_PROFIT_BUSINESS


def test_calculate_pre_assessment_value_for_loss_business(loss_business):
    value = calculate_preassessment_value(loss_business)
    assert value == APPROVAL_RATE_LOSS_BUSINESS


def test_calculate_pre_assessment_value_for_business_with_more_assets(business_with_asset_greater_than_loan_amount):
    value = calculate_preassessment_value(business_with_asset_greater_than_loan_amount)
    assert value == APPROVAL_RATE_BUSINESS_WITH_LARGE_ASSETS
