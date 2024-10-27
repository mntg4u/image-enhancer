from flask import Flask, request, render_template, send_file, jsonify
import os
import base64
import requests
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ENHANCED_FOLDER'] = 'enhanced/'

# Create directories for uploads and enhanced images
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['ENHANCED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enhance', methods=['POST'])
def enhance():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    user_id = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], f"{user_id}.jpeg")
    file.save(path)

    with open(path, 'rb') as f:
        photo = f.read()

    encoded_image_data = base64.b64encode(photo).decode('utf-8')

    # Define API endpoint and headers
    url = 'https://apis-awesome-tofu.koyeb.app/api/remini?mode=enhance'
    headers = {'Content-Type': 'application/json'}
    data = {"imageData": encoded_image_data}

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            enhanced_path = os.path.join(app.config['ENHANCED_FOLDER'], f"enhanced_{user_id}.jpeg")
            with open(enhanced_path, 'wb') as f:
                f.write(response.content)

            return send_file(enhanced_path, as_attachment=True)
        else:
            return jsonify({'error': f"Error: {response.text}"})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

