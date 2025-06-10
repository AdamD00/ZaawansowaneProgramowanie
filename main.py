import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
from YOLOInterface import findLicensePlateOnIMG
import OCR
import cv2
import time


def crop_box(box):
    x1, y1, x2, y2 = map(int, box[0])
    return y1, y2, x1, x2


def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2


def show_plate(image, detected_text, ground_truth, title):

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"OCR: {detected_text} | GT: {ground_truth} | {title}")
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    plates_dict = {}
    tree = ET.parse("annotations.xml")
    root = tree.getroot()

    for image in root.findall("image"):
        image_name = image.get("name")
        for box in image.findall("box"):
            for attr in box.findall("attribute"):
                if attr.get("name") == "plate number":
                    plates_dict[image_name] = attr.text.strip()

    positiveTests = 0
    testCounter = 0
    start_time = time.time()

    for j in range(40, 141):  # zmień zakres przy większej liczbie zdjęć
        filename = f'{j}.jpg'
        pngPath = f'photos/{filename}'
        img = cv2.imread(pngPath)

        try:
            cropped = findLicensePlateOnIMG(img,pngPath)
            preprocessed = OCR.preprocess(cropped)
            if preprocessed is None:
                print(f"{filename}: ❌ Brak tablicy (preprocess)")
                continue

            text = OCR.fastPlateOCR(preprocessed)
            label = plates_dict.get(filename, "")

            print(f"{filename}: 🔡 OCR = {text}, ✅ GT = {label}")
           # show_plate(cropped, text, label, "Paddle")

            testCounter += 1
            if label == text:
                positiveTests += 1
        except Exception as e:
            print(f"{filename}: ❌ Błąd przetwarzania: {e}")

    total_time = time.time() - start_time
    accuracy = (positiveTests / testCounter) * 100 if testCounter > 0 else 0
    print(f"\n🔍 Accuracy: {accuracy:.2f}%")
    print(f"⏱️ Time: {total_time:.2f} seconds")

    final_grade = calculate_final_grade(accuracy, total_time)
    print(f"📊 Final Grade: {final_grade}")
