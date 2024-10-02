import yaml
import os

file_path = os.environ.get("INPUT_PATH", "location.yaml")

with open(file_path, "r") as file:
    data = yaml.safe_load(file)
for location in data["locations"]:
    for store_name, details in location.items():
        address = details[0]["주소"]
        print(f"{store_name},{address}")
