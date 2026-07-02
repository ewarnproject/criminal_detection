import cv2
import threading


class CameraStream:

    def __init__(self, name, rtsp_url):
        self.name = name
        self.rtsp_url = rtsp_url

        self.cap = cv2.VideoCapture(rtsp_url)

        self.frame = None
        self.running = False

        self.thread = threading.Thread(target=self.update)

    def start(self):
        self.running = True
        self.thread.start()

    def update(self):

        while self.running:

            ret, frame = self.cap.read()

            if ret:
                self.frame = frame

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()