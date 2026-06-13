import json
FILE = "robot_data.json"
def read_data():
    with open(FILE, "r") as f:
        return json.load(f)
def write_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
