import yaml

with open("location.yaml", "r") as file:
    data = yaml.safe_load(file)
for location in data["locations"]:
    for store_name, details in location.items():
        print(store_name)
        print(details)
        address = details[0]["주소"]
        print(f"{store_name},{address}")
