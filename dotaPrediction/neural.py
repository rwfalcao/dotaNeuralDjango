import numpy as np
from keras.utils import to_categorical
from keras import models
from keras import layers
from keras.models import load_model
from keras.models import model_from_json
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.staticfiles.storage import staticfiles_storage

def neuralNetwork(compArray):
  model = load_model('dotaPrediction/neuralModels/categoricalModel.h5')
  
  compArray = [compArray]
  predictedWinner = model.predict(np.array(compArray))

  return predictedWinner