import os
from ultralytics import YOLO




def train():
    model = YOLO("yolo11n.pt")

    dir = os.getcwd()
    data_path = os.path.join(dir,'data.yaml')

    train_results=model.train(
        data=data_path,
        epochs=50,
        #imgsz=640,
        device='cuda'
    )

    print("Training finished. Res:", train_results)

if __name__ == '__main__':
    train()