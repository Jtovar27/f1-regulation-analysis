import requests
import json

def get_race_results(year):
    all_races = []
    offset = 0 
    limit = 100 
    while True:
        url = f"https://api.jolpi.ca/ergast/f1/{year}/results/?limit=500&format=json"
        response = requests.get(url)
        data = response.json()

        races = data["MRData"]["RaceTable"]["Races"]
        total = int(data["MRData"]["total"])

        all_races.extend(races)
        offset += limit

        if offset >= total:
            break

    return {"MRData": {"RaceTable": {"Races": all_races}}}

def save_raw_data(data, year):
    with open(f"data/raw/{year}.json","w") as f:
        json.dump(data, f, indent=4)