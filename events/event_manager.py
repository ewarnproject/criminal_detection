from datetime import datetime


class EventManager:

    def __init__(self):

        self.active_events = set()

        print("Event Manager Ready")

    def trigger(self, camera, event_type, person_id):

        key = (camera, event_type, person_id)

        # Event already active
        if key in self.active_events:
            return False

        self.active_events.add(key)

        timestamp = datetime.now().strftime("%H:%M:%S")

        if person_id is None:
            person = "Unknown"
        else:
            person = f"Person-{person_id:03d}"

        print("\n===================================")
        print(f"TIME   : {timestamp}")
        print(f"CAMERA : {camera}")
        print(f"EVENT  : {event_type}")
        print(f"PERSON : {person}")
        print("===================================\n")

        return True

    def clear(self, camera, event_type, person_id):

        key = (camera, event_type, person_id)

        self.active_events.discard(key)