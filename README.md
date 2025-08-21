# Cat-or-not-Cat: A small app to detect whether an uploaded image is of a cat or not 🐱
This is a simple Flask web application that uses the pretrained MobileNetV2 model to clas
This is a simple Flask web application that uses the pretrained MobileNetV2 model to classify whether an uploaded image contains a cat. The model is loaded with ImageNet weights and performs inference on user-uploaded images via a web interface.

## Features

- Uses TensorFlow Keras MobileNetV2 pretrained on ImageNet
- Detects if an image contains a cat based on classification labels
- Returns the top prediction label and confidence score

## Installation

1. Clone the repository(use these commands in cmd, power shell etc):
   git clone <repository-url>
   cd <repository-folder>

2. Create and activate a Python virtual environment:
  python -m venv venv
  # On Windows: venv\Scripts\activate

3. Install dependencies:
  pip install -r requirements.txt

## Usage

1. Run the Flask app: python app.py
2. Open your browser and go to: http://localhost:5000/
3. Upload an image to check if it contains a cat. The result will show if a cat was detected, the predicted label, and confidence.









