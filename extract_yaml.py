import yaml

with open("location.yaml", "r") as file:
    data = yaml.safe_load(file)
for location in data["locations"]:
    for store_name, details in location.items():
        address = details["주소"]
        print(f"{store_name},{address}")
