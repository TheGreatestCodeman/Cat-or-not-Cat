# Cat-or-not-Cat: A small app to detect whether an uploaded image is of a cat or not 🐱
This is a simple Flask web application that uses the pretrained MobileNetV2 model to clas
## Features
- Uses TensorFlow Keras MobileNetV2 pretrained on ImageNet
- Detects if an image contains a cat based on classification labels
- Returns the top prediction label and confidence score
- Simple REST API endpoint `/predict` accepting image uploads
- Web interface served at `/` to upload images and see results

## Installation
### 1. Clone the repository  
Open a terminal (Command Prompt, PowerShell, or shell) on your local machine, then run:
  git clone repository-url
  cd repository-folder
Replace `<repository-url>` with the actual GitHub repo link.
### 2. Create and activate a Python virtual environment (optional but recommended)
Still in your terminal, run:
- On Windows (Command Prompt):
   python -m venv venv
   venv\Scripts\activate

### 3. Install dependencies
With the virtual environment activated, run in the terminal:
   "pip install -r requirements.txt"
If you don’t have a `requirements.txt`, instead run:
   "pip install Flask tensorflow pillow numpy"
## Usage
### 4. Run the Flask app
Run this command in the same terminal (with the virtual environment active and inside the project folder):
   "python app.py"
You should see output showing the Flask server running, usually on:
   "http://localhost:5000/"
### 5. Access the app
Open a web browser and navigate to:
   "http://localhost:5000/"









