import cv2


class CameraManager:

    def __init__(self, camera_urls):
        self.camera_urls = camera_urls
        self.captures = {}

    def connect_all(self):
        """
        Connect to all cameras.
        """

        for name, url in self.camera_urls.items():

            cap = cv2.VideoCapture(url)

            if cap.isOpened():
                print(f"✅ Connected : {name}")
                self.captures[name] = cap

            else:
                print(f"❌ Failed : {name}")

    def read_frames(self):
        """
        Read one frame from every connected camera.
        """

        frames = {}

        for name, cap in self.captures.items():

            ret, frame = cap.read()

            if ret:
                frames[name] = frame

        return frames

    def release_all(self):

        for cap in self.captures.values():
            cap.release()

        cv2.destroyAllWindows()