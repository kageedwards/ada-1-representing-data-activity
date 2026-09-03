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
    output = {}
    for registration in registrations:
        year = registration["year"]
        event_type = registration["event_type"]

        # Add a dictionary for this year in needed
        if year not in output: 
            output[year] = {}

        # Add an inner list for this event type in needed
        if event_type not in output[year]:
            output[year][event_type] = []

        # Add a tuple to the [year][event_type] inner list
        inner_item = ( registration["attendee"], registration["scholarship_tier"] )
        output[year][event_type].append(inner_item)

    return output


    # for registration in registrations:
    #     for key, item in registration.items():
    #         if not output[year]:
    #             output[year] = {}

    #         if not output[year][event]


def list_event_types(conference_data, year):
    """Part B, Q1: Return a list of every event type offered in a given year."""
    output = []

    for key, event in conference_data.items():
        for event_type, attendees in event.items():
            if key == year:
                output.append(event_type)

    return output


def total_attendance(conference_data, year):
    """Part B, Q2: Return the total number of sign-ups (all event types) for a given year."""
    output = {}

    for event_type, attendees in conference_data[year].items():
        if event_type not in output:
            output[event_type] = 0

        output[event_type] += len(attendees)

    return output

def get_scholarship_attendees(conference_data, year):
    """Part B, Q3: Return a list of names of attendees who used a scholarship ticket in a given year."""
    output = {}
    
    for event_type, attendees in conference_data[year].items():
        for (name, scholarship) in attendees:
            if scholarship:
                if scholarship not in output:
                            output[scholarship] = []

                if name not in output[scholarship]:
                    output[scholarship].append(name)

    return output

def most_popular_event_type(conference_data):
    """Part B, Q4: Return the event type with the most total sign-ups across all years."""
    output = {}
    highest_value = 0

    # Iterating over each year, but we don't need to access the year
    for year, event in conference_data.items():
        # For each event type in this year's sign-ups...
        for event_type, attendees in event.items():
            # Start a count if we don't have event type in the dict yet
            if event_type not in output:
                output[event_type] = 0

            # Add the number of sign-ups for this year / event_type
            output[event_type] += len(attendees)

    return output



if __name__ == "__main__":
    conference_data = reshape_conference_data(registrations)
    print("Nested conference data:")
    pprint(conference_data)

    print("2021 event types:", list_event_types(conference_data, 2021))
    print("2023 total attendance:", total_attendance(conference_data, 2023))
    print("2024 scholarship attendees:", get_scholarship_attendees(conference_data, 2024))
    print("Most popular event type:", most_popular_event_type(conference_data))
