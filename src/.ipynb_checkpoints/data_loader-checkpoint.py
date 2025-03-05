import os
from skimage.io import imread

def read_images(image_folder, label):
    """
    Reads all images from the provided folder and returns them as a list of NumPy arrays
    with the corresponding label.

    Arguments:
    image_folder -- The path to the folder containing images.
    label -- The label for these images (e.g., 'no' or 'yes').

    Returns:
    A tuple: List of images (NumPy arrays), and a list of corresponding labels.
    """
    images = []
    labels = []
    for filename in os.listdir(image_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            image_path = os.path.join(image_folder, filename)
            image = imread(image_path)  # Reads image as a NumPy array
            images.append(image)
            labels.append(label)
    
    return images, labels