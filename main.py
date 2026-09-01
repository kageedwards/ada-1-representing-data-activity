"""
Cool Dev Conf -- Nested Data Lab

Run this file from your terminal with:
    python3 main.py

As you implement each function below, its print statement at the bottom of
this file will start showing real output instead of None.
"""

from pprint import pprint

# Raw registration records exported from the Cool Dev Conf database.
# Each dict is one attendee signing up for one event in one year.
registrations = [
    {"year": 2021, "event_type": "long talk", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2021, "event_type": "workshop", "attendee": "Jordan", "scholarship_tier": None},
    {"year": 2021, "event_type": "panel", "attendee": "Alicia", "scholarship_tier": None},
    {"year": 2022, "event_type": "workshop", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2022, "event_type": "affinity group", "attendee": "Jordan", "scholarship_tier": None},
    {"year": 2022, "event_type": "long talk", "attendee": "Sam", "scholarship_tier": None},
    {"year": 2023, "event_type": "short talk", "attendee": "Priya", "scholarship_tier": None},
    {"year": 2023, "event_type": "workshop", "attendee": "Sam", "scholarship_tier": None},
    {"year": 2023, "event_type": "panel", "attendee": "Devon", "scholarship_tier": None},
    {"year": 2024, "event_type": "workshop", "attendee": "Priya", "scholarship_tier": "community"},
    {"year": 2024, "event_type": "long talk", "attendee": "Devon", "scholarship_tier": "full-ride"},
    {"year": 2024, "event_type": "panel", "attendee": "Sam", "scholarship_tier": "partial"},
    {"year": 2024, "event_type": "short talk", "attendee": "Riley", "scholarship_tier": "community"},
]


def reshape_conference_data(registrations):
    """
    Part A: Turn the flat `registrations` list into a nested dictionary shaped like:
        conference_data[year][event_type] -> list of (attendee, scholarship_tier) tuples

    Example:
        conference_data[2021]["long talk"] -> [("Priya", None)]
    """
    pass


def list_event_types(conference_data, year):
    """Part B, Q1: Return a list of every event type offered in a given year."""
    pass


def total_attendance(conference_data, year):
    """Part B, Q2: Return the total number of sign-ups (all event types) for a given year."""
    pass


def most_popular_event_type(conference_data):
    """Part B, Q3: Return the event type with the most total sign-ups across all years."""
    pass


def get_scholarship_attendees(conference_data, year):
    """Part B, Q4: Return a list of names of attendees who used a scholarship ticket in a given year."""
    pass


if __name__ == "__main__":
    conference_data = reshape_conference_data(registrations)
    print("Nested conference data:")
    pprint(conference_data)

    print("2021 event types:", list_event_types(conference_data, 2021))
    print("2023 total attendance:", total_attendance(conference_data, 2023))
    print("Most popular event type:", most_popular_event_type(conference_data))
    print("2024 scholarship attendees:", get_scholarship_attendees(conference_data, 2024))
