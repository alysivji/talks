from http import HTTPStatus
import requests

resp = requests.get("https://gbfs.divvybikes.com/gbfs/en/station_status.json")
STATION_ID = "286"


def bikes_left_nested():
    if resp.status_code == HTTPStatus.OK:
        station_data = resp.json()["data"]["stations"]

        for station in station_data:
            if station["station_id"] == STATION_ID:
                if station["num_bikes_available"] <= 3:
                    return "Hurry up! Bikes are almost out!"
                else:
                    return "No need to rush just yet."
    else:
        resp.raise_for_status()


def bikes_left_guard_clause():
    if resp.status_code != HTTPStatus.OK:
        resp.raise_for_status()

    station_data = resp.json()["data"]["stations"]
    for station in station_data:
        if station["station_id"] != STATION_ID:
            continue

        if station["num_bikes_available"] <= 3:
            return "Hurry up! Bikes are almost out!"
        return "No need to rush just yet."
