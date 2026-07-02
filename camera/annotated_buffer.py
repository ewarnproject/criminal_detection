import threading


class AnnotatedBuffer:

    def __init__(self):
        self.frames = {}
        self.lock = threading.Lock()

    def update(self, camera_name, frame):
        with self.lock:
            self.frames[camera_name] = frame

    def get(self, camera_name):
        with self.lock:
            return self.frames.get(camera_name)

    def get_all(self):
        with self.lock:
            return dict(self.frames)