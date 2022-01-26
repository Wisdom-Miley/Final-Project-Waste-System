# Import Dependencies
from flask import Flask, render_template, request, redirect, flash, url_for
import main
import urllib.request
from werkzeug.utils import secure_filename
from main import getPrediction
import os
import templates


#################################################
# Flask Setup
#################################################

UPLOAD_FOLDER = '\Data Analyst\waste-classification-model-main/static/uploads'

app = Flask(__name__)                    

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to HTML    

# Route to HTML    
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods = ['POST']) #/file
# Our function for pushing the image to the classifier model
def submit_image():
     if request.method == 'POST':
          if 'file' not in request.files:
               flash('No file part')
               return redirect(request.url)
          file = request.files['file']
        # Error message if no file submitted
          if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        # Return results predictive data
          if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('static/uploads'))
            getPrediction(filename)
            answer, probability_results, filename = getPrediction(filename)
            flash(answer)
            flash(probability_results) # accuracy
            flash(filename)
            return redirect('/')
            result=predict(file.filename)
                #os.remove(filename)
          if redirect=="":
            error="Sorry!"
            return templates('index.html', file=file,error=error)
 

if __name__ == "__main__":
    app.run(debug=True)
