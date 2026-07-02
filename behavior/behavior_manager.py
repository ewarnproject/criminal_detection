from behavior.intrusion import IntrusionDetector


class BehaviorManager:

    def __init__(self):

        self.intrusion = IntrusionDetector()

        print("Behavior Manager Ready")

    def process(self, tracks, zones):

        intrusions, left_zone, active_intruders = self.intrusion.check(
            tracks,
            zones
        )

        return {
            "intrusions": intrusions,
            "left_zone": left_zone,
            "active_intruders": active_intruders
        }