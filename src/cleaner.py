import json

def load_raw_data(year):
    with open(f"data/raw/{year}.json", "r") as f:
        data = json.load(f)
    return data

def extract_results(data, year):
    races = data["MRData"]["RaceTable"]["Races"]
    records = []
    
    for race in races:
        race_name = race["raceName"]
        round_number = race["round"]

        for result in race["Results"]:
            record = {
                "year": year,
                "race": race_name,
                "round": round_number,
                "driver": result["Driver"]["code"],
                "grid": int(result["grid"]),
                "position": result["positionText"],
                "points": float(result["points"]),
                "status": result["status"]
            }
            records.append(record)
    return records