from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
# from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from panda_file import df




# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# Step 3: Vectorize the text data
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Step 4: Train the model using Logistic Regression
model = LogisticRegression(max_iter=200)
model.fit(X_train_vectorized, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")

# Step 6: Predict new texts
new_texts = [
    "$1000 sale revenue from selling books",      # Expected: income
    "Rent paid for bookstore location",          # Expected: expenses
    "purchase of new book invetory",             # Expected: exp
]

# Vectorize new texts
X_new = vectorizer.transform(new_texts)

# Predict categories for new texts
predictions = model.predict(X_new)

for text, category in zip(new_texts, predictions):
    print(f"Text: '{text}' => Predicted Category: {category}")