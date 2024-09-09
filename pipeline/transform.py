"""Script to transform the downloaded data."""

import pandas as pd
import json

FILEPATH = "data/nasa_eva_records.json"


def read_json_file() -> list[dict]:
    """Returns a list of dicts containing the EVA json data."""
    with open(FILEPATH, mode="r", encoding="utf-8") as f:
        json_data = json.load(f)

    return json_data


def turn_crew_into_lists(eva_events: list[dict]) -> None:
    """"""
    eva_event_results = []

    for eva_event in eva_events:
        names = eva_event["crew"].split("  ")
        eva_event["crew"] = [name.strip() for name in names if name]
        if len(eva_event["crew"]) > 1:
            for crew_member in eva_event["crew"]:
                eva_event_copy = eva_event.copy()
                eva_event_copy["crew"] = crew_member
                eva_event_results.append(eva_event_copy)
        else:
            eva_event["crew"] = eva_event["crew"][0]
            eva_event_results.append(eva_event)

    return eva_event_results


def clean_vehicle_names(eva_events: list[dict]):
    """"""
    for eva_event in eva_events:
        vehicles = eva_event["vehicle"].split("  ")
        eva_event["vehicle"] = "/".join([vehicle.strip()
                                        for vehicle in vehicles if vehicle])

    return eva_events


def save_as_csv():
    pass


if __name__ == "__main__":
    eva_json_data = read_json_file()
    eva_data = turn_crew_into_lists(eva_json_data)
    print(clean_vehicle_names(eva_data))
