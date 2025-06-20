import cv2
import re
from paddleocr import PaddleOCR
from fast_alpr import ALPR

from matplotlib import pyplot as plt
#ocr_model = PaddleOCR(use_angle_cls=True, lang='en')
alpr = ALPR(
    detector_model="yolo-v9-t-384-license-plate-end2end",
    ocr_model="global-plates-mobile-vit-v2-model",
)


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

    return cleaned_text

'''

def fastPlateOCR(image):

    if len(image.shape) ==2:
        image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)

    result = ocr_model.ocr(image)

    if result and len(result[0]) > 0:
        text = result[0][0][1][0]
        # Oczyść tekst: tylko A-Z i 0-9
        text = ''.join(filter(str.isalnum, text.upper()))
        clean_text = clean_license_plate_text(text)
        return clean_text
    else:
        return ""
'''
def alprOCR(image):
    result = alpr.predict(image)
    return result[0].ocr.text







