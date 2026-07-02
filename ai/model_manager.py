from ultralytics import YOLO


class ModelManager:

    def __init__(self):

        print("Loading YOLO11...")

        self.model = YOLO("yolo11n.pt")

        print("YOLO Ready")

    def get_model(self):

        return self.model