import cv2
from camera.camera_manager import CameraManager
from config import CAMERAS
from ai.detector import ObjectDetector

def main():

    # Create Camera Manager
    manager = CameraManager(CAMERAS)

    # Connect to all cameras
    manager.connect_all()
    detector = ObjectDetector()

    while True:

        frames = manager.read_frames()

        if not frames:
            print("No frames received.")
            break

        display_frames = []

        for camera_name, frame in frames.items():

            # AI Detection
         annotated_frame = detector.detect(frame)

             # Resize
         annotated_frame = cv2.resize(
         annotated_frame,
         (640, 360)
          )

          # Camera Name 
         cv2.putText(
         annotated_frame,
         camera_name,
         (20, 35),
         cv2.FONT_HERSHEY_SIMPLEX,
         1,
         (0, 255, 0),
         2
          )

         display_frames.append(annotated_frame)

        if len(display_frames) == 3:

            top = cv2.hconcat([display_frames[0], display_frames[1]])

            blank = display_frames[0].copy()
            blank[:] = (40, 40, 40)

            bottom = cv2.hconcat([display_frames[2], blank])

            final = cv2.vconcat([top, bottom])

        elif len(display_frames) == 2:

            final = cv2.hconcat(display_frames)

        else:

            final = display_frames[0]

        cv2.imshow("CADMS V2", final)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            print("Closing CADMS...")
            break

    manager.release_all()


if __name__ == "__main__":
    main()