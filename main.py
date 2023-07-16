import cv2
import pytesseract
import numpy as np
from langdetect import detect
from langcodes import standardize_tag
from pdf2image import convert_from_path

def preprocess_image(image):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to enhance text regions
    threshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 5)

    # Perform morphological operations to enhance text quality
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(threshold, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    return eroded


def extract_text_from_image(image, lang=''):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection to detect lines
    edges = cv2.Canny(grayscale, 50, 150, apertureSize=3)

    # Apply probabilistic Hough line transform to find the dominant lines
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    # Calculate the average angle of the detected lines
    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi
        angles.append(angle)
    avg_angle = np.mean(angles)

    # Rotate the image to correct the text orientation
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Apply additional preprocessing to enhance text quality
    preprocessed = preprocess_image(rotated)

    # Use Tesseract to extract the text from the rotated and preprocessed image
    if lang == '':
        extracted_text = pytesseract.image_to_string(preprocessed)
    else:
        extracted_text = pytesseract.image_to_string(preprocessed, lang=lang)

    # Return the extracted text and average rotation angle
    return extracted_text, avg_angle

def extract_text_from_pdf(pdf_path, lang=''):
    # Convert each page of the PDF into an image
    images = convert_from_path(pdf_path)

    extracted_text = []

    # Process each image (page) of the PDF
    for image in images:
        # Convert PIL image to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Extract text from the image (page)
        text, angle = extract_text_from_image(image_cv, lang=lang)

        # Store the extracted text
        extracted_text.append(text)

    return extracted_text

# Usage example
image_path = './samples/deskew-1.png'
image_path = './samples/invoice-sample.jpg'
image = cv2.imread(image_path)
extracted_text, rotation_angle = extract_text_from_image(image)
# extracted_text, rotation_angle = extract_text_from_image(image, lang='deu')
print("Extracted Text:", extracted_text)

# file_path = './samples/text-sample.pdf'
# extracted_text= extract_text_from_pdf(file_path, lang='lat')
# print("Extracted Text:", extracted_text)
