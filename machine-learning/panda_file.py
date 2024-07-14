import pandas as pd

# Sample data
data = {
    "text": [
        "Received salary for the month",
        "Bought groceries",
        "Paid credit card bill",
        "Income from side business",
        "Monthly rent payment",
        "Loan repayment",
        "Sold old furniture",
        "Dining out with friends",
        "Mortgage payment due",
        "Freelance project earnings",
        "Sold stocks for profit",            # INCOME
        "Bought new shoes",                  # EXPENSES
        "Paid off my car loan",              # DEBT
        "Salary increase this quarter",      # INCOME
        "Annual subscription fee",           # EXPENSES
        "Refinanced my mortgage",            # DEBT
        "Earnings from rental property",     # INCOME
        "Dinner at a fancy restaurant",      # EXPENSES
        "Credit card debt accumulation",     # DEBT
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
        "DEBT"
    ]
}


# Add more labeled data to your dataset
more_data = {
    "text": [
        "Received monthly dividend",       # INCOME
        "Paid for internet service",       # EXPENSES
        "Settled personal loan",           # DEBT
        "Income from freelance work",      # INCOME
        "Groceries for the week",          # EXPENSES
        "Paid off student loan",           # DEBT
    ],
    "label": [
        "INCOME", "EXPENSES", "DEBT", "INCOME", "EXPENSES", "DEBT"
    ]
}


# Combine data into DataFrame
more_df = pd.DataFrame(more_data)
df = pd.DataFrame(data)
df = pd.concat([df, more_df], ignore_index=True)
