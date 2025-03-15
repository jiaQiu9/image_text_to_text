import cv2
import pytesseract
import numpy as np

#import pytesseract

# Set the path to Tesseract (check with `which tesseract`)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Configure Tesseract Path (Windows Users may need to set this)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """Preprocess image to enhance OCR accuracy"""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary

def extract_text(image_path):
    """Extracts text while trying to maintain formatting"""
    processed_image = preprocess_image(image_path)
    custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode and Page Segmentation Mode
    text = pytesseract.image_to_string(processed_image, config=custom_config)
    return text

# Run OCR
if __name__ == "__main__":
    image_path = "test_image.jpg"  # Change to your image file
    extracted_text = extract_text(image_path)
    print("Extracted Text:\n")
    print(extracted_text)
