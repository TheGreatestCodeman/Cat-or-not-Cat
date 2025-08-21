from flask import Flask, render_template, request, jsonify
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

model = MobileNetV2(weights="imagenet")

def is_cat(img):
    img = img.resize((224, 224)) 
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]

  
    for _, label, prob in decoded:
        if "cat" in label.lower():
            return True, label, float(prob)
    return False, decoded[0][1], float(decoded[0][2])
    
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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


