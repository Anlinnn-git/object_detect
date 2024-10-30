import os
from flask import Flask, render_template, request, redirect, url_for
from detector import run_detector
from utils import resize_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Update this to point to the static/uploads folder

# Ensure static/uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Simulating an image history list
image_history = []
output_history = []  # List to keep track of processed output images

@app.route('/')
def index():
    return render_template('index.html', uploaded_image=None, result_image=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Resize image before processing
        resized_image_path = resize_image(filepath)

        # Run object detection on the image
        result_image_path = run_detector(resized_image_path)

        # Add uploaded image to history
        image_history.append(file.filename)  # Keep track of uploaded images
        output_history.append(os.path.basename(result_image_path))  # Keep track of output images

        # Extract only the filename for display, not the full path
        return render_template('index.html', 
                               uploaded_image=file.filename, 
                               result_image=os.path.basename(result_image_path))

    return redirect(request.url)

@app.route('/recent')
def recent():
    # Render a page showing recent input images
    return render_template('recent.html', images=image_history)  # Pass the image history to the template

@app.route('/recent_outputs')
def recent_outputs():
    # Render a page showing recent output images
    return render_template('recent_outputs.html', outputs=output_history)  # Pass the output history to the template

if __name__ == '__main__':
    app.run(debug=True)
