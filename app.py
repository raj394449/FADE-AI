from flask import Flask, request, render_template
from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import os

app = Flask(__name__)

# Ensure 'uploads' directory exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the deepfake detection model
model_name = "Wvolf/ViT_Deepfake_Detection"
model = ViTForImageClassification.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template("index.html", error="No image uploaded")

    image_file = request.files['image']
    
    if image_file.filename == '':
        return render_template("index.html", error="No file selected")
    
    # Save uploaded file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(file_path)

    # Load and preprocess the image
    image = Image.open(file_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    # Determine classification
    classification = model.config.id2label[predicted_class]
    return render_template("result.html", classification=classification)

if __name__ == '__main__':
    app.run(debug=True)
