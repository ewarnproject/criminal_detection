import csv
import os

LOG_FILE = "logs/events.csv"


def get_events():

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, newline="", encoding="utf-8") as file:

        events = list(csv.DictReader(file))

        events.reverse()      # newest first

        return events


def get_statistics():

    events = get_events()

    stats = {

        "cameras": len(set(e["Camera"] for e in events)),

        "events": len(events),

        "intrusions": len(
            [e for e in events if e["Event"] == "INTRUSION"]
        ),

        "evidence": len(
            [e for e in events if e["Evidence"]]
        )

    }

    return stats