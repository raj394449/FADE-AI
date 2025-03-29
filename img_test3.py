# This Model Gives the correct predication

from transformers import ViTForImageClassification, ViTImageProcessor
from PIL import Image
import torch

# Load the model and processor
model = ViTForImageClassification.from_pretrained("Wvolf/ViT_Deepfake_Detection")
processor = ViTImageProcessor.from_pretrained("Wvolf/ViT_Deepfake_Detection")

# Load and preprocess the image
image = Image.open("test_01.jpg").convert("RGB")
# image = Image.open("test.jpg").convert("RGB")
inputs = processor(images=image, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

# Map class index to label
label = model.config.id2label[predicted_class]
print(f"Predicted Label: {label}")