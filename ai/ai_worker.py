import threading
import time

from config import CAMERAS
from config_zones import ZONES

from ai.v2.model_manager import ModelManager
from ai.v2.detector import Detector

from behavior.behavior_manager import BehaviorManager
from events.event_manager import EventManager

from renderer.renderer import Renderer
from evidence.evidence_manager import EvidenceManager

from logs.event_logger import EventLogger
from system.system_health import health


class AIWorker:

    def __init__(self, frame_buffer, annotated_buffer):

        self.frame_buffer = frame_buffer
        self.annotated_buffer = annotated_buffer

        self.running = False

        print("Loading AI Engine...")

        # One detector per camera
        self.detectors = {}

        for camera_name in CAMERAS:

            model = ModelManager().get_model()
            self.detectors[camera_name] = Detector(model)

        health.total_cameras = len(CAMERAS)
        

        self.behavior_manager = BehaviorManager()
        self.event_manager = EventManager()
        self.evidence_manager = EvidenceManager()
        self.event_logger = EventLogger()
        self.renderer = Renderer()

        print("AI Engine Ready.")
        

    def start(self):

        self.running = True

        health.update(

             ai_running=True,

             model_loaded=True,

             connected=len(CAMERAS),

             total=len(CAMERAS)

        )

        

        threading.Thread(
            target=self.process,
            daemon=True
        ).start()

    def process(self):

        while self.running:

            frames = self.frame_buffer.get_all()

            for name, frame in frames.items():

                try:

                    # ----------------------------
                    # AI Detection
                    # ----------------------------
                    tracks = self.detectors[name].detect(frame)

                    # ----------------------------
                    # Camera Zones
                    # ----------------------------
                    zones = ZONES.get(name, [])

                    # ----------------------------
                    # Intrusion Detection
                    # ----------------------------
                    results = self.behavior_manager.process(
                        tracks,
                        zones
                    )

                    intrusions = results["intrusions"]

                    left_zone = results["left_zone"]

                    active_intruders = results["active_intruders"]


                    # ----------------------------
                    # Trigger Events
                    # ----------------------------
                    for intrusion in intrusions:

                        created = self.event_manager.trigger(
                            camera=name,
                            event_type="INTRUSION",
                            person_id=intrusion["id"]
                        )

                         # Save Evidence Snapshot
                        if created and intrusion["id"] is not None:

                            evidence_path = self.evidence_manager.save_snapshot(
                                frame=frame,
                                camera=name,
                                person_id=intrusion["id"]
                            )

                            self.event_logger.log(
                                camera=name,
                                event_type="INTRUSION",
                                person_id=intrusion["id"],
                                evidence_path=evidence_path

                            )    




                    # ----------------------------
                    # Clear Events
                    # ----------------------------
                    for person_id in left_zone:

                        self.event_manager.clear(
                            camera=name,
                            event_type="INTRUSION",
                            person_id=person_id
                        )

                    # ----------------------------
                    # Render Final Frame
                    # ----------------------------
                    annotated = self.renderer.render(
                        frame=frame,
                        tracks=tracks,
                        zones=zones,
                        intruder_ids=active_intruders
                    )

                    # ----------------------------
                    # Display
                    # ----------------------------
                    self.annotated_buffer.update(
                        name,
                        annotated
                    )

                except Exception as e:

                    print(f"AI Error ({name}): {e}")

            time.sleep(0.01)

    def stop(self):

        self.running = False

        health.update(

            ai_running=False,

            model_loaded=False,

            connected=0,

            total=len(CAMERAS)

        )