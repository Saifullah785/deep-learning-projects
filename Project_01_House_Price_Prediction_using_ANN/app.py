from flask import Flask, render_template, request
import pickle
import numpy as np
from tensorflow.keras.models import load_model