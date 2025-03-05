import sys
import os

# Add the 'src' folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now you can import your modules from 'src'
from data_loader import read_images
from image_processing import preprocess_image
from feature_extraction import extract_features
from model_training import train_model
from utils import save_model, load_model

# Define paths for dataset (replace with actual paths)
dataset_path_no = './data/no/'
dataset_path_yes = './data/yes/'

# Step 1: Load images
images_no, labels_no = read_images(dataset_path_no, label='no')
images_yes, labels_yes = read_images(dataset_path_yes, label='yes')

# Combine the data
images = images_no + images_yes
labels = labels_no + labels_yes

# Step 2: Preprocess images
processed_images = [preprocess_image(image) for image in images]

# Step 3: Extract features from the images
features = [extract_features(image) for image in processed_images]

# Step 4: Train the model (Example: Neural Network or other model)
model = train_model(features, labels)

# Step 5: Save the trained model (optional)
save_model(model, 'tumor_detection_model.pkl')

# Step 6: Load the trained model (example for inference later)
loaded_model = load_model('tumor_detection_model.pkl')

# For testing the model with a new image (example):
# image_to_predict = preprocess_image('path_to_new_image')
# feature_to_predict = extract_features(image_to_predict)
# prediction = loaded_model.predict([feature_to_predict])

print("Model training and saving complete.")