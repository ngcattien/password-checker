import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample data
passwords = [
    ("123456", "Weak"), ("password", "Weak"), ("qwerty", "Weak"),
    ("P@ssw0rd", "Medium"), ("LetMeIn123", "Medium"),
    ("G!bR@lt@r2022", "Strong"), ("Str0ngP@$$w0rd!2023", "Strong")
]

# Prepare data
X, y = zip(*passwords)
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1,3))
X = vectorizer.fit_transform(X)

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model and vectorizer
joblib.dump((vectorizer, model), 'password_strength_model.pkl')
print("Model trained and saved successfully.")
