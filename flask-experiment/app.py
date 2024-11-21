from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

# Flask setup
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load ML model
model = joblib.load('color_model.pkl')

# Folder to store uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save the file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract dominant color
    try:
        dominant_color = extract_dominant_color(file_path)
        hex_code = model.predict([dominant_color])[0]  # Predict hex code
        return jsonify({
            'dominant_color': dominant_color.tolist(),
            'hex_code': hex_code
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
