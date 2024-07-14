import pandas as pd


data = {
    "text": [
        "Received salary for the month",  # INCOME
        "Bought groceries",  # EXPENSES
        "Paid credit card bill",  # DEBT
        "Income from side business",  # INCOME
        "Monthly rent payment",  # EXPENSES
        "Loan repayment",  # DEBT
        "Sold old furniture",  # INCOME
        "Dining out with friends",  # EXPENSES
        "Mortgage payment due",  # DEBT
        "Freelance project earnings",  # INCOME
        "Sold stocks for profit",  # INCOME
        "Bought new shoes",  # EXPENSES
        "Paid off my car loan",  # DEBT (paid off, so no longer debt)
        "Salary increase this quarter",  # INCOME
        "Annual subscription fee",  # EXPENSES
        "Refinanced my mortgage",  # DEBT
        "Earnings from rental property",  # INCOME
        "Dinner at a fancy restaurant",  # EXPENSES
        "Credit card debt accumulation",  # DEBT
    ],
    "label": [
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "EXPENSES",
        "DEBT",
    ],
}

more_data = {
    "text": [
        "Received monthly dividend",  # INCOME
        "Paid for internet service",  # EXPENSES
        "Settled personal loan",  # DEBT (paid off, so no longer debt)
        "Income from freelance work",  # INCOME
        "Groceries for the week",  # EXPENSES
        "Paid off student loan",  # DEBT (paid off, so no longer debt)
    ],
    "label": [
        "INCOME",
        "EXPENSES",
        "DEBT",
        "INCOME",
        "EXPENSES",
        "DEBT",
    ],
}

# Combine data into a single DataFrame
df = pd.concat([pd.DataFrame(data), pd.DataFrame(more_data)], ignore_index=True)