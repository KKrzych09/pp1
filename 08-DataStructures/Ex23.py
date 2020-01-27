import json

with open ("notowania.json", "r") as file:
    json.load(file)
    
    with open('notowania.json', 'w') as f:
        json.dump(data, f, indent=4)
        