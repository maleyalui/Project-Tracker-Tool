import json
import os

folder = "data/data.json"


def load_data():
    if not os.path.exists(folder):
        return {"users": []}
    
    try:
        with open(folder, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warining: Corrupted data file. Resetting.")
        return {"users" : []}
    

def save_data(data):

    os.makedirs("data", exist_ok=True)

    with open(folder, "w") as file:
        json.dump(data, file, indent=4)