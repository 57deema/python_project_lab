import numpy as np
from skimage.filters import sobel, prewitt, gaussian
from skimage import filters
from skimage.morphology import disk
from skimage import img_as_ubyte
from skimage.transform import resize
from skimage.color import rgb2gray
from tqdm import tqdm

# Filter functions
def entropy(image, disk_obj):
    """
    Calculate the entropy of the image using the disk-based neighborhood.
    """
    return filters.rank.entropy(img_as_ubyte(image), disk_obj)

def sobel_filter(image):
    """
    Apply the Sobel filter for edge detection.
    """
    return sobel(image)

def prewitt_filter(image):
    """
    Apply the Prewitt filter for edge detection.
    """
    return prewitt(image)

def gaussian_filter(image, sigma):
    """
    Apply the Gaussian filter with the given sigma value for smoothing.
    """
    return gaussian(image, sigma=sigma)

def preprocess_image(image, target_size=(128, 128)):
    """
    Preprocess an image by resizing it and converting to grayscale.

    Arguments:
    image -- The image to preprocess (a NumPy array).
    target_size -- The target size for resizing the image (default is 128x128).

    Returns:
    A preprocessed grayscale image (128x128).
    """
    # Resize image
    image_resized = resize(image, target_size, anti_aliasing=True)

    # Handle different image formats
    if image_resized.ndim == 3 and image_resized.shape[-1] == 4:  # If RGBA, remove alpha
        image_resized = image_resized[..., :3]
    if image_resized.ndim == 3 and image_resized.shape[-1] == 3:  # Convert RGB to grayscale
        image_gray = rgb2gray(image_resized)
    else:  # Already grayscale
        image_gray = image_resized

    return image_gray

# Function to apply filters to a list of images
def process_images(images):
    """
    Process a list of images by applying various filters: Sobel, Prewitt, Gaussian, and Entropy.

    Arguments:
    images -- A list of images (each image is expected to be a NumPy array).

    Returns:
    A list of dictionaries where each dictionary contains the filtered images.
    """
    processed_images = []

    for image in tqdm(images):
        # Preprocess the image first (resize and convert to grayscale)
        preprocessed_image = preprocess_image(image)

        # Apply filters and store results in a dictionary
        filtered_images = {
            'Original': image,
            'Preprocessed': preprocessed_image,
            'Entropy': entropy(preprocessed_image, disk(2)),  # Apply entropy on the preprocessed image
            'Gaussian': gaussian_filter(preprocessed_image, sigma=1),  # Apply Gaussian filter
            'Sobel': sobel_filter(preprocessed_image),  # Apply Sobel edge detection filter
            'Prewitt': prewitt_filter(preprocessed_image)  # Apply Prewitt edge detection filter
        }

        processed_images.append(filtered_images)

    return processed_images