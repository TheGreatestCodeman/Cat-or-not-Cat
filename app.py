from flask import Flask, render_template, request, jsonify
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Load pretrained MobileNetV2
model = MobileNetV2(weights="imagenet")

# Function to check if image is a cat
def is_cat(img):
    img = img.resize((224, 224))  # Resize to model input
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]

    # Check if any prediction contains "cat"
    for _, label, prob in decoded:
        if "cat" in label.lower():
            return True, label, float(prob)
    return False, decoded[0][1], float(decoded[0][2])

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    img = Image.open(io.BytesIO(file.read()))
    cat, label, prob = is_cat(img)
    return jsonify({"is_cat": cat, "label": label, "confidence": prob})

if __name__ == "__main__":
    app.run(debug=True)
