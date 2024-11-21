from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from utils.color_extraction import extract_dominant_color

def extract_dominant_color(image_path, n_colors=1):
    """
    Extracts the dominant color from an image using KMeans clustering.
    
    Parameters:
        image_path (str): Path to the image file.
        n_colors (int): Number of clusters/colors to find. Default is 1.

    Returns:
        np.array: Dominant RGB color as an integer array.
    """
    # Open image and convert to RGB
    image = Image.open(image_path).convert('RGB')
    image = image.resize((150, 150))  # Resize for faster computation
    data = np.array(image).reshape(-1, 3)  # Flatten pixels into RGB values

    # Use KMeans to find dominant color
    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init='auto')
    kmeans.fit(data)
    return kmeans.cluster_centers_[0].astype(int)  # Return RGB of dominant color
