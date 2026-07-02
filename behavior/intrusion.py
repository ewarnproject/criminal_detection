class IntrusionDetector:

    def __init__(self):

        print("Intrusion Detector Ready")

        # Remember active intrusions
        self.active_intrusions = set()

    def inside_zone(self, cx, cy, zone):

        return (
            zone["x1"] <= cx <= zone["x2"]
            and
            zone["y1"] <= cy <= zone["y2"]
        )

    def check(self, tracks, zones):

        intrusions = []
        current_ids = set()

        for track in tracks:

            x1, y1, x2, y2 = track["bbox"]

            if track["id"] is None:
                 continue

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            for zone in zones:

                if self.inside_zone(cx, cy, zone):

                    if track["id"] is not None:
                        current_ids.add(track["id"])

                    if track["id"] not in self.active_intrusions:

                        intrusions.append({
                            "id": track["id"],
                            "bbox": track["bbox"],
                            "center": (cx, cy),
                            "zone": zone["name"]
                        })

        # -----------------------------
        # This MUST be OUTSIDE both loops
        # -----------------------------

        left_zone = self.active_intrusions - current_ids

        self.active_intrusions = current_ids

        return intrusions, left_zone, current_ids