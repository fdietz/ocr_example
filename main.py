import cv2
import pytesseract

# Load image
# img = cv2.imread("./images/invoice-sample.jpg")
img = cv2.imread("./images/hitchhikers-rotated.png")
# img = cv2.imread("./images/greek-thai.png")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold to convert to binary image
threshold_img = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Pass the image through pytesseract
text = pytesseract.image_to_string(threshold_img)

# Print the extracted text
print(text)
