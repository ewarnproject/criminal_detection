import os
import cv2
from datetime import datetime


class EvidenceManager:

    def __init__(self):

        self.root = "evidence"

        os.makedirs(self.root, exist_ok=True)

        print("Evidence Manager Ready")

    def save_snapshot(self, frame, camera, person_id):

        now = datetime.now()

        date_folder = now.strftime("%Y-%m-%d")

        folder = os.path.join(
            self.root,
            date_folder,
            camera
        )

        os.makedirs(folder, exist_ok=True)

        filename = f"{now.strftime('%H-%M-%S')}_Person-{person_id:03d}.jpg"

        filepath = os.path.join(
            folder,
            filename
        )

        cv2.imwrite(
            filepath,
            frame
        )

        print()

        print("Snapshot Saved")
        print(filepath)

        print()

        return filepath