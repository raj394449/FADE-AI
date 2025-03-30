🚀 Deepfake Image Detector (FADE-AI)
A Flask-based web application that detects deepfake images using a pre-trained Vision Transformer (ViT) model. Upload an image, and the model will classify it as Real or Deepfake.


📂 Project Directory Structure
Deepfake-Detector/
│── static/
│   ├── style.css        # CSS for UI styling
│   ├── script.js        # JavaScript for UI validation
│── templates/
│   ├── index.html       # Upload page
│   ├── result.html      # Result page
│── uploads/             # (Stores uploaded images)
│── app.py               # Flask backend
│── requirements.txt     # Required dependencies
│── README.md            # Project description (this file)


📌 Features
✅ Deepfake Detection: Classifies images as Real or Deepfake
✅ Pre-trained Transformer Model: Uses ViT_Deepfake_Detection for accurate predictions
✅ Simple Web Interface: Built using HTML, CSS, and JavaScript
✅ Fast & Lightweight: Runs efficiently on CPU/GPU


📦 Dependencies
Install required dependencies using:
pip install -r requirements.txt


🛠️ Modules Used
Flask → Web framework for hosting the app
Torch (PyTorch) → Handles deep learning model inference
Transformers → Loads the Vision Transformer (ViT) model
Pillow (PIL) → Processes uploaded images


🧠 Pre-trained Model
Model Name: Wvolf/ViT_Deepfake_Detection
Type: Vision Transformer (ViT)
Task: Image Classification (Real vs. Deepfake)
Source: 🤗 Hugging Face


⚡ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/Deepfake-Detector.git
cd Deepfake-Detector

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask application
python app.py

4️⃣ Open in browser
Go to: http://127.0.0.1:5000/


🎯 How It Works
1️⃣ Upload an image via the web interface
2️⃣ Model analyzes the image and classifies it
3️⃣ Results displayed: "Real" or "Deepfake"


📌 Screenshots



📝 Future Improvements
🔹 Add support for video deepfake detection
🔹 Improve accuracy with custom fine-tuning
🔹 Deploy on cloud platforms (AWS/GCP)


🛡️ License
MIT License. Free to use and modify.


⭐ Contribute
Feel free to submit issues or contribute to improvements.