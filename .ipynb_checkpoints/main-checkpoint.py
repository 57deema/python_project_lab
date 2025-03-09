import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.utils import save_model, load_model

# Add the 'src' folder to the system path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(src_path)

# Debugging: Ensure 'src/' exists
if not os.path.exists(src_path):
    raise FileNotFoundError(f"🚨 Error: 'src/' folder not found! Expected at {src_path}")

# Debugging: Check if utils.py exists
utils_path = os.path.join(src_path, "utils.py")
if not os.path.exists(utils_path):
    raise FileNotFoundError("🚨 Error: 'utils.py' not found in 'src/' folder!")

# Import modules from 'src'
from data_loader import read_images
from image_processing import preprocess_image
from feature_extraction import process_images as extract_features
from model_training import train_and_validate_model as train_model

# Define paths for dataset
dataset_path_no = './data/no/'
dataset_path_yes = './data/yes/'

# Step 1: Load images
images_no, labels_no = read_images(dataset_path_no, label=0)  # '0' for no tumor
images_yes, labels_yes = read_images(dataset_path_yes, label=1)  # '1' for tumor

# Debugging: Ensure images are loaded correctly
if not images_no or not images_yes:
    raise ValueError("🚨 Error: No images were loaded. Check dataset paths!")

# Combine the data
images = images_no + images_yes
labels = labels_no + labels_yes

# Step 2: Preprocess images
processed_images = [preprocess_image(image) for image in images]

# Debugging: Ensure images are preprocessed correctly
if not processed_images or len(processed_images) != len(images):
    raise ValueError("🚨 Error: Image preprocessing failed. Check `preprocess_image()`!")

# Step 3: Extract features from the images
features_yes = extract_features(processed_images[:len(images_yes)], tumor_presence=1)
features_no = extract_features(processed_images[len(images_yes):], tumor_presence=0)

# Debugging: Print one extracted feature dictionary
if features_yes:
    print(f"✅ Example Extracted Features: {list(features_yes[0].keys())}")

# Ensure extracted features are not empty
if not features_yes or not features_no or len(features_yes[0]) <= 1:
    raise ValueError("🚨 Error: Feature extraction failed! No valid features extracted.")

features = features_yes + features_no  # Merge tumor & non-tumor features

# Convert features to DataFrame
df = pd.DataFrame(features)

# Debugging: Ensure DataFrame is correctly structured
print(f"✅ DataFrame Shape: {df.shape}")
print(df.head())

if df.empty or df.shape[1] == 1:  # Only 'Tumor' column exists, no features
    raise ValueError("🚨 Error: Feature DataFrame contains no extracted features!")

# Ensure 'Tumor' column is correctly assigned
if 'Tumor' not in df.columns:
    print("🚨 Warning: 'Tumor' column missing! Assigning manually...")
    df['Tumor'] = labels

# Debugging: Print label distribution
print(f"✅ Label Distribution: \n{df['Tumor'].value_counts()}")

# Handle missing values (important for ML models)
df.fillna(0, inplace=True)

# Step 4: Split the dataset into training and testing
X = df.drop(columns=['Tumor'])  # Features
y = df['Tumor']  # Target labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Debugging: Ensure dataset is not empty
print(f"✅ Dataset Sizes - X_train: {X_train.shape}, y_train: {y_train.shape}")
if X_train.empty or y_train.empty:
    raise ValueError("🚨 Error: X_train or y_train is empty. Check feature extraction and dataset preprocessing!")

# Step 5: Train the model (Using RandomForestClassifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train and validate the model
train_results = train_model(model, X_train, X_test, y_train, y_test)

# Step 6: Save the trained model (optional)
save_model(model, 'tumor_detection_model.pkl')

# Step 7: Load the trained model (for later inference)
loaded_model = load_model('tumor_detection_model.pkl')

# Debugging: Ensure model is correctly saved and loaded
if not loaded_model:
    raise ValueError("🚨 Error: Model loading failed. Check `save_model()` and `load_model()`!")

# Display results
print("✅ Model training and saving complete.")
print(f"🎯 Training Results: {train_results}")