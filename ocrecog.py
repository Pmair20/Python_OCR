import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'<path to the tesseract exe>'       # path to the tesseract exe after installing from the link mentioned in setup_link txt
img = cv2.imread('<path to the image to be used for OCR>')                                  # path to the text image to use OCR
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)                                    # converting to gray scale(black and white) for better recognition
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)
kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)                                     # remove noise around the characters
img = cv2.dilate(img, kernel, iterations=1)
output = pytesseract.image_to_string(img)                                    #running OCR on the converted image
print("OUTPUT:", output)                                                     #printing the text extracted from the image
