# Dependencies
import numpy as np
import os
import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import VGG16
import tensorflow as tf
from flask import Flask, render_template, request, jsonify,abort
from PIL import Image

app= Flask (__name__)
UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def predict(img_path):
def getPrediction(filename):
     model = tf.keras.models.load_model("static/model/model.h5")
     img = load_img('\Data Analyst\waste-classification-model-main/static/uploads/Biodegradable.jpg/'+filename, target_size=(180, 180))
     img = img_to_array(img)
     img = img / 255
     img = np.expand_dims(img,axis=0)
     category = model.predict_classes(img)
     answer = category[0]
     probability = model.predict(img)
     probability_results = 0

     if answer == 1:
          answer = "Recycle"
          probability_results = probability[0][1]
     else:
          answer = "Biodegradable"
          probability_results = probability[0][0]

     answer = str(answer)
     probability_results=str(probability_results)

     values = [answer, probability_results, filename]
     return values[0], values[1], values[2]


if __name__ == "__main__":
    app.run(debug=True)