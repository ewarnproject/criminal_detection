class Detector:

    def __init__(self, model):
        self.model = model

    def detect(self, frame):

        results = self.model.track(
            source=frame,
            conf=0.40,
            classes=[0],
            persist=True,
            verbose=False
        )

        result = results[0]

        tracks = []

        if result.boxes is not None:

            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                track_id = None

                if box.id is not None:
                    track_id = int(box.id[0])

                tracks.append({
                    "id": track_id,
                    "bbox": (x1, y1, x2, y2)
                })

        return tracks