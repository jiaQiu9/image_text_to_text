import cv2
import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Load image
image_path = "test_image.jpg"  # Change this to your actual image path
image = cv2.imread(image_path)

def preprocess_image(image):
    """Enhance the image for better OCR accuracy."""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize to improve OCR accuracy (Tesseract works better on larger text)
    height, width = gray.shape
    scaling_factor = 2  # Increase size for better text detection
    gray = cv2.resize(gray, (width * scaling_factor, height * scaling_factor), interpolation=cv2.INTER_LINEAR)
    
    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Use adaptive histogram equalization to enhance contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    # Apply sharpening filter
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(gray, -1, kernel)

    # Apply binary thresholding
    _, binary = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological transformations to refine text edges
    kernel = np.ones((1,1), np.uint8)
    processed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    
    return processed

def extract_text(image):
    """Extract text using Tesseract OCR with optimized settings."""
    custom_config = r'--oem 3 --psm 4 -c preserve_interword_spaces=1'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text.strip()

# Preprocess the image
processed_image = preprocess_image(image)

# Extract text
final_text = extract_text(processed_image)

# Print extracted text
print("Extracted Text:\n")
print(final_text)