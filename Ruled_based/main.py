import re

from dataset import income_keywords, expenses_keywords, debt_keywords


def combined_keywords(keywords_dict):
    combined_keywords = []
    for keyword in keywords_dict.values():
        combined_keywords.extend(keyword)
    return combined_keywords


income_keywords_combined = combined_keywords(income_keywords)
expenses_keywords_combined = combined_keywords(expenses_keywords)
debt_keywords_combined = combined_keywords(debt_keywords)

# Data Preprocessing: Normalize the transaction text
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '*', text)
    return text


# Keyword Matching: Check for the presence of keywords
def keyword_match(text, keyword_list):
    for keyword in keyword_list:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            return True
    return False

# Classification function
def classify_transaction(transaction):
    transaction = normalize_text(transaction)
    
    if keyword_match(transaction, income_keywords_combined):
        return "INCOME"
    elif keyword_match(transaction, expenses_keywords_combined):
        return "EXPENSES"
    elif keyword_match(transaction, debt_keywords_combined):
        return "DEBT"
    else:
        return "UNKNOWN"


# Example transactions
transactions = [
    "Received monthly salary of $3000",
    "Paid $50 for groceries",
    "Credit card balance of $2000",
    "Interest earned from savings account",
    "Utility bill payment of $100"
]

# Classify each transaction
for transaction in transactions:
    category = classify_transaction(transaction)
    print(f"Transaction: {transaction} => Category: {category}")




