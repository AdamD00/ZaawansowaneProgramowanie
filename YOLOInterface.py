from ultralytics import YOLO
def findLicensePlateOnIMG(image,nameImage,conf_threshold=0.25):
    model = YOLO("best.pt")
    results = model(nameImage,conf=conf_threshold)
    xyxy = results[0].boxes.xyxy.cpu().numpy()
    x1, y1, x2, y2 = map(int, xyxy[0])
    return image[y1:y2,x1:x2]
