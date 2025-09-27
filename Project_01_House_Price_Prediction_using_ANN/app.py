from flask import Flask, render_template, request
import pickle
import numpy as np
from tensorflow.keras.models import load_model


# Now you can use this model to make predictions

# Initialize the Flask app
app = Flask(__name__)

# Load the model and scaler using pickle
# Load the model
model = load_model('model_ann.h5')
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)
