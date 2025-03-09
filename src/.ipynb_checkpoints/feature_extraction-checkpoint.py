import numpy as np
import skimage.feature as feature

def compute_glcm_features(image, filter_name):
    """
    Computes GLCM (Gray Level Co-occurrence Matrix) features for an image.
    """
    image = (image * 255).astype(np.uint8)

    # Debugging: Check if image is valid before extracting features
    if image is None or image.size == 0:
        print(f"🚨 Warning: Received an empty image for filter {filter_name}.")
        return {}

    graycom = feature.graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    # Debugging: Print the raw GLCM matrix to ensure it's computed
    print(f"✅ GLCM Matrix ({filter_name}): {graycom.shape}")

    features = {}
    for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']:
        try:
            values = feature.graycoprops(graycom, prop).flatten()
            for i, value in enumerate(values):
                features[f'{filter_name}_{prop}_{i+1}'] = value
        except Exception as e:
            print(f"🚨 Error computing {prop} for {filter_name}: {e}")

    # Debugging: Print extracted features before returning
    if features:
        print(f"✅ Extracted Features for {filter_name}: {list(features.keys())}")
    else:
        print(f"🚨 No features extracted for {filter_name}.")

    return features

def process_images(images_list, tumor_presence):
    """
    Extract GLCM features from filtered images and add a tumor label.

    Arguments:
    images_list -- A list of dictionaries containing filtered images.
    tumor_presence -- Label (1 for tumor, 0 for no tumor).

    Returns:
    A list of dictionaries with extracted GLCM features.
    """
    glcm_features_list = []
    
    for filtered_images in images_list:
        glcm_features = {}

        if isinstance(filtered_images, dict):
            for key, image in filtered_images.items():
                extracted_features = compute_glcm_features(image, key)
                
                if extracted_features and not glcm_features:
                    print(f"✅ Extracted GLCM Features ({key}): {list(extracted_features.keys())}")

                glcm_features.update(extracted_features)

        if not glcm_features:
            print(f"🚨 Error: No GLCM features extracted for one image. Skipping...")
            continue

        glcm_features['Tumor'] = tumor_presence
        glcm_features_list.append(glcm_features)

    if not glcm_features_list:
        raise ValueError("🚨 Error: No valid GLCM features were extracted.")

    return glcm_features_list