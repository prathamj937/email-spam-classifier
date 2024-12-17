from flask import Flask, request, jsonify, send_from_directory
import joblib
import os

# Initialize Flask app
app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Load the model and vectorizer from the 'model' folder
model_path = os.path.join("model", "email_spam_classifier.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Serve the index.html as the main page
@app.route("/")
def serve_index():
    return send_from_directory("frontend", "index.html")

# Serve static files like CSS and JS
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("frontend", filename)

# API Endpoint for Predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email = data.get("email", "")

    if not email:
        return jsonify({"error": "No email text provided"}), 400

    # Transform the input email
    X_email = vectorizer.transform([email])
    prediction = model.predict(X_email)
    result = "Spam" if prediction[0] == 'spam' else "Not Spam"

    return jsonify({"result": result})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
