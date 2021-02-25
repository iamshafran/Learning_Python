import json

with open("Learn/Python Tutorial - Corey Schafer/states.json") as f:
    data = json.load(f)

for state in data["states"]:
    del state["area_codes"]

with open("Learn/Python Tutorial - Corey Schafer/new_states.json", "w") as f:
    json.dump(data, f, indent=2)
