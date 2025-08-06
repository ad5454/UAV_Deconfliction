import json

def load_mission_data(path):
    with open(r"C:\Users\Admin\Downloads\primary_mission.json") as file:
        return json.load(file)

def load_simulated_flights(path):
    with open(r"C:\Users\Admin\Downloads\simulated_flights.json") as file:
        return json.load(file)
