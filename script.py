import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load your dataset (replace 'emails.csv' with your actual dataset)
df = pd.read_csv("cleaned_data.csv",encoding="latin-1")  # Ensure this file contains a "text" column

# Train CountVectorizer
vectorizer = CountVectorizer(stop_words="english", max_features=5000)
vectorizer.fit(df["data"])  # Fit on the email text data

# Save the vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")
print("Vectorizer saved successfully!")
