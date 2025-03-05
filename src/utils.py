import time
import numpy as np
import joblib

def save_model(model, filename):
    """
    Saves the trained model to a file.
    """
    joblib.dump(model, filename)
    
def load_model(filename):
    """
    Loads a trained model from a file.
    """
    return joblib.load(filename)