import requests
import json

def get_race_results(year):
    url = f"https://api.jolpi.ca/ergast/f1/{year}/results/?limit=500&format=json"
    response = requests.get(url)
    data = response.json()
    return data

def save_raw_data(data, year):
    with open(f"data/raw/{year}.json","w") as f:
        json.dump(data, f, indent=4)