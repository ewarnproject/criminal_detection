import cv2


class Renderer:

    def __init__(self):
        print("Renderer Ready")

    def render(self, frame, tracks, zones, intruder_ids):

        annotated = frame.copy()

        # -----------------------------
        # Draw Restricted Zones
        # -----------------------------
        for zone in zones:

            cv2.rectangle(
                annotated,
                (zone["x1"], zone["y1"]),
                (zone["x2"], zone["y2"]),
                (0, 0, 255),
                2
            )

            cv2.putText(
                annotated,
                zone["name"],
                (zone["x1"], zone["y1"] - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

        intrusion_found = False

        # -----------------------------
        # Draw Persons
        # -----------------------------
        for track in tracks:

            x1, y1, x2, y2 = track["bbox"]
            person_id = track["id"]

            is_intruder = (
                person_id is not None and
                person_id in intruder_ids
            )

            if is_intruder:
                color = (0, 0, 255)
                label = f"INTRUDER-{person_id:03d}"
                intrusion_found = True
            else:
                color = (0, 255, 0)

                if person_id is None:
                    label = "Person"
                else:
                    label = f"Person-{person_id:03d}"

            cv2.rectangle(
                annotated,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            cv2.putText(
                annotated,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

        # -----------------------------
        # Alert Banner
        # -----------------------------
        if intrusion_found:

            cv2.rectangle(
                annotated,
                (0, 60),
                (annotated.shape[1], 105),
                (0, 0, 255),
                -1
            )

            cv2.putText(
                annotated,
                "INTRUSION DETECTED",
                (15, 92),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 255),
                2
            )

        return annotated