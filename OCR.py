import numpy as np
import pytesseract
import easyocr
import cv2
import re
from fast_plate_ocr import ONNXPlateRecognizer
from paddleocr import PaddleOCR

from matplotlib import pyplot as plt
ocr_model = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

def clean_license_plate_text(text):
    if not text:
        return ""

    text = text.upper()
    text = ''.join(text.split())

    valid_chars = re.compile(r'[A-Z0-9]')
    cleaned_text = ''.join(c for c in text if valid_chars.match(c))

    char_replacements = {
        'O': '0', 'I': '1', 'B': '8', 'S': '5', 'Z': '2', 'G': '6', 'D': '0',
    }

    return cleaned_text


def tesseractOCR(image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(image, config=custom_config)
    clean_text = clean_license_plate_text(text)
    return clean_text

def easyOCR(image):
    reader = easyocr.Reader(['en'])
    text = reader.readtext(image,detail=0)
    try:
        clean_text =clean_license_plate_text(text[0])
    except:
        print("Text not find")
        clean_text = ""
    return clean_text
def fastPlateOCR(image):

    if len(image.shape) ==2:
        image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)

    result = ocr_model.ocr(image, cls=True)

    if result and len(result[0]) > 0:
        text = result[0][0][1][0]
        # Oczyść tekst: tylko A-Z i 0-9
        text = ''.join(filter(str.isalnum, text.upper()))
        clean_text = clean_license_plate_text(text)
        return clean_text
    else:
        return ""








