import nltk
nltk.download('stopwords')
import random
import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE
import joblib

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Define the examples for each category
income_examples = [
    "Received salary for the month", "Income from side business", "Sold old furniture", 
    "Freelance project earnings", "Sold stocks for profit", "Salary increase this quarter", 
    "Earnings from rental property", "Monthly dividend received", "Bonus for completed projects", 
    "Investment interest income", "Profit from sale of assets", "Cashback from credit card", 
    "Government subsidy received", "Pension payment", "Royalties from book sales", 
    "Referral bonus", "Tax refund received", "Income from consulting", "Gift from family", 
    "Won a prize", "End-of-year bonus", "Inheritance money", "Selling homemade crafts", 
    "Freelance writing payment", "Side job income", "Commission from sales", 
    "Cash gift for birthday", "Stock dividends", "Affiliate marketing earnings", "Money from rent"
]

expenses_examples = [
    "Bought groceries","Paid for car repair", "Monthly rent payment", "Dining out with friends", "Bought new shoes","Annual subscription fee", "Dinner at a fancy restaurant", "Paid for internet service", "Groceries for the week", "Utility bill payment", "Car maintenance costs", "Medical bills", "Subscription renewal", "Gym membership fee", "Clothing purchase", "Vacation expenses", 
    "Entertainment costs", "Gas bill payment", "Household repairs", "Education expenses", 
    "Water bill", "Electricity bill", "New phone purchase", "Charity donation", 
    "Furniture purchase", "Insurance premium", "Movie tickets", "Shopping for clothes", 
    "Travel expenses", "Subscription to streaming service", "Pet care expenses"
]

debt_examples = [
    "Paid credit card bill", "Loan repayment", "Mortgage payment due", 
    "Credit card debt accumulation", "Settled personal loan", "Paid off student loan", 
    "Refinanced my mortgage", "Car loan repayment", "Student loan payment", 
    "Debt consolidation payment", "Paying off mortgage", "Credit card interest", 
    "Car financing payment", "Personal loan repayment", "Medical loan payment", 
    "Home equity loan payment", "Loan from bank", "Debt repayment to family", 
    "Consolidation loan payment", "Loan for home renovation", "Paying down line of credit", 
    "Bridge loan payment", "Vacation loan repayment", "Loan for business startup", 
    "Settling overdue bills", "Finance agreement payment", "Credit line repayment", 
    "Loan installment payment", "Emergency loan repayment", "Short-term loan payment"
]

# Function to create synthetic data
def create_synthetic_data(num_samples, income_examples, expenses_examples, debt_examples):
    data = {"text": [], "label": []}
    for _ in range(num_samples):
        category = random.choice(["INCOME", "EXPENSES", "DEBT"])
        if category == "INCOME":
            data["text"].append(random.choice(income_examples))
            data["label"].append("INCOME")
        elif category == "EXPENSES":
            data["text"].append(random.choice(expenses_examples))
            data["label"].append("EXPENSES")
        else:
            data["text"].append(random.choice(debt_examples))
            data["label"].append("DEBT")
    return data

# Create additional 1000 synthetic data points
additional_data = create_synthetic_data(1000, income_examples, expenses_examples, debt_examples)


# Combine synthetic data with any existing data
new_data = additional_data

# Convert to DataFrame
df = pd.DataFrame(new_data)

# Stop words setup
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Apply preprocessing
df['cleaned_text'] = df['text'].apply(preprocess_text)

# Split the data
X = df['cleaned_text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Balance the training data using SMOTE
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_vec, y_train)

# Hyperparameter tuning using Grid Search
parameters = {
    'C': [0.1, 1, 10, 100],
    'solver': ['newton-cg', 'lbfgs', 'liblinear']
}

model = LogisticRegression()
clf = GridSearchCV(model, parameters, cv=5, scoring='f1_weighted')
clf.fit(X_train_balanced, y_train_balanced)
best_model = clf.best_estimator_

# Train the best model
best_model.fit(X_train_balanced, y_train_balanced)

# Predict and evaluate
y_pred = best_model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
joblib.dump(best_model, 'logistic_regression_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
