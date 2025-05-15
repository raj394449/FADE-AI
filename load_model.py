# This Model is gives the correct prediction for images but accuracy is not accurate.

# Load model directly from Huggingface.co
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("Wvolf/ViT_Deepfake_Detection")
model = AutoModelForImageClassification.from_pretrained("Wvolf/ViT_Deepfake_Detection")