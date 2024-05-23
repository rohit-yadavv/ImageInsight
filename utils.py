import cv2
import pytesseract
from pytesseract import Output

def extract_text(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to perform OCR on the image
    text_data = pytesseract.image_to_data(gray, output_type=Output.DICT)

    # Extract text and concatenate into a single paragraph
    extracted_text = " ".join([text_data['text'][i] for i in range(len(text_data['text'])) if text_data['text'][i].strip()])

    return extracted_text

def segment_visual_elements(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment visual elements
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours of segmented visual elements
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    segmented_image = image.copy()
    cv2.drawContours(segmented_image, contours, -1, (0, 255, 0), 2)

    return segmented_image
