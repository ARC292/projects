from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Define the upload folder
app.config['UPLOAD_FOLDER'] = 'upload'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the pre-trained model
model = load_model('model/inseptfinal.h5')

# Define the class labels
class_labels = [
    'AnnualCrop', 
    'Forest', 
    'HerbaceousVegetation', 
    'Highway', 
    'Industrial', 
    'Pasture', 
    'PermanentCrop', 
    'Residential', 
    'River', 
    'SeaLake'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded image
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Prepare the path for the JPG version
        image_name = os.path.splitext(file.filename)[0] + '.jpg'
        file_path_jpg = os.path.join(app.config['UPLOAD_FOLDER'], image_name)

        # Convert the image to JPG format if needed
        img = Image.open(file_path)
        if img.format != 'JPEG':
            img = img.convert('RGB')
            img.save(file_path_jpg, 'JPEG')
        else:
            # If the image is already in JPEG format, set file_path_jpg to the original path
            file_path_jpg = file_path

        # Preprocess the image for the model
        img = Image.open(file_path_jpg)
        img = img.resize((299, 299))  # Resize as required by the model
        img = np.array(img) / 255.0   # Normalize the image
        img = np.expand_dims(img, axis=0)

        # Predict the class
        prediction = model.predict(img)
        predicted_class = class_labels[np.argmax(prediction)]

        # Redirect to the result page with the prediction and image name
        return render_template('result.html', prediction=predicted_class, image=image_name)

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
