from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS 
import onnxruntime as ort
import numpy as np

# Load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load ONNX model session
session = ort.InferenceSession("email_classifier.onnx")

# Get input and output names
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

app = Flask(__name__, template_folder='frontend')

CORS(app)

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()
        email_text = data.get("email", "")

        if not email_text:
            return jsonify({"error": "No email text provided"}), 400

        # Vectorize email
        email_vector = vectorizer.transform([email_text])
        email_array = email_vector.toarray().astype(np.float32)

        # ONNX prediction
        prediction = session.run([output_name], {input_name: email_array})[0][0]
        result = "Spam" if prediction == 1 else "Not Spam"

        return jsonify({"result": result})

    except Exception as e:
        print("Prediction error:", e)
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
