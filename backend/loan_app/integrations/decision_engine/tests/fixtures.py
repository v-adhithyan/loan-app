import random

import pytest
from faker import Faker


@pytest.fixture
def profit_business():
    faker = Faker()
    business_name = faker.name()
    established_year = random.randint(1500, 2020)
    loan_amount = random.randint(1000000, 5000000)

    balance_sheet = []

    for month in range(1, 13):
        balance_sheet.append({
            'year': 2020,
            'month': month,
            'profitOrLoss': random.randint(1000, 10000),
            'assetsValue': random.randint(1000, 5000)
        })

    return {
        'business_name': business_name,
        'established_year': established_year,
        'loan_amount': loan_amount,
        'balance_sheet': balance_sheet
    }


@pytest.fixture()
def loss_business():
    faker = Faker()
    business_name = faker.name()
    established_year = random.randint(1500, 2020)
    loan_amount = random.randint(1000000, 5000000)

    balance_sheet = []

    for month in range(1, 13):
        balance_sheet.append({
            'year': 2020,
            'month': month,
            'profitOrLoss': random.randint(-10000, -1000),
            'assetsValue': random.randint(1000, 5000)
        })

    return {
        'business_name': business_name,
        'established_year': established_year,
        'loan_amount': loan_amount,
        'balance_sheet': balance_sheet
    }


@pytest.fixture
def business_with_asset_greater_than_loan_amount():
    faker = Faker()
    business_name = faker.name()
    established_year = random.randint(1500, 2020)
    loan_amount = random.randint(10000, 50000)

    balance_sheet = []

    for month in range(1, 13):
        balance_sheet.append({
            'year': 2020,
            'month': month,
            'profitOrLoss': random.randint(-10000, -1000),
            'assetsValue': 60000
        })

    return {
        'business_name': business_name,
        'established_year': established_year,
        'loan_amount': loan_amount,
        'balance_sheet': balance_sheet
    }
