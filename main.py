from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# make sure the directory to save files is created and defined
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# route to handle the file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # save the file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return jsonify({"message": "File uploaded successfully!", "filename": file.filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
