import numpy as np
from skimage import filters

def augment_feature_stack(image):
    """
    Function that creates a multi-dimensional image 
    with the original pixel values and a gaussian and 
    sobel blurred arrays
    """
    gaussian = filters.gaussian(image, sigma=3)
    edges = filters.sobel(gaussian)

    # Create feature stack with 1D arrays:
    feature_stack = [
        image.ravel(),
        gaussian.ravel(),
        edges.ravel()
    ]

    return np.asarray(feature_stack)

def format_data(feature_stack, annotation):
    # reformat the data to match what scikit-learn expects
    # transpose the feature stack
    X = feature_stack.T
    # make the annotation 1-dimensional
    y = annotation.ravel()
    
    # remove all pixels from the feature and annotations which have not been annotated
    mask = y > 0
    X = X[mask]
    y = y[mask]

    return X, y