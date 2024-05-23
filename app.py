from flask import Flask, request, render_template, send_from_directory
import os
import cv2
from config import UPLOAD_FOLDER, OUTPUT_FOLDER
from utils import extract_text, segment_visual_elements

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(file_path)

        # Extract text and segment visual elements
        extracted_text = extract_text(file_path)
        segmented_image = segment_visual_elements(file_path)

        # Save segmented image
        segmented_image_filename = 'segmented_' + filename
        segmented_image_path = os.path.join(app.config['OUTPUT_FOLDER'], segmented_image_filename)
        cv2.imwrite(segmented_image_path, segmented_image)

        return render_template('output.html', extracted_text=extracted_text, segmented_image_filename=segmented_image_filename)

@app.route('/output/<filename>')
def output_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
