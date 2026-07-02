import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open one RTSP camera
cap = cv2.VideoCapture("rtsp://admin:ISDR%40430@192.168.50.157:8554/Streaming/Channels/102")

if not cap.isOpened():
    print("Failed to open camera.")
    exit()

print("Press Q to quit.")

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.40,
        verbose=False
    )

    result = results[0]

    print("--------------------------------")

    if result.boxes is not None:
        print("is_track:", result.boxes.is_track)
        print("IDs:", result.boxes.id)

    annotated = result.plot()

    cv2.imshow("Tracker Test", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()