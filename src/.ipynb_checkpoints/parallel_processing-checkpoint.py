import time
import numpy as np
from multiprocessing import Pool, cpu_count
from image_processing import process_images
from feature_extraction import process_images as process_features

def process_single_image(filtered_images, tumor_presence):
    glcm_features = {}
    for key, image in filtered_images.items():
        glcm_features.update(compute_glcm_features(image, key))
    glcm_features['Tumor'] = tumor_presence
    return glcm_features

def process_images_parallel(images_list, tumor_presence):
    with Pool(cpu_count()) as pool:
        results = pool.starmap(process_single_image, [(filtered_images, tumor_presence) for filtered_images in images_list])
    return results