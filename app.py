from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS 

# Load vectorizer and model
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("email_classifier.pkl", "rb"))

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    email_text = data.get("email", "")

    if not email_text:
        return jsonify({"error": "No email text provided"}), 400

    # Transform text using CountVectorizer
    email_vector = vectorizer.transform([email_text])
    
    # Predict
    prediction = model.predict(email_vector)[0]
    result = "Spam" if prediction == 1 else "Not Spam"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
