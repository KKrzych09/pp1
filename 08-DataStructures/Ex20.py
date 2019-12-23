import json

computer = {
    "RAM": "8GB",
    "ROM": "128GB",
    "LCD screen": "True",
    "Numeric keyboard": "False",
    "Resolution": "15\""
}

with open("komputer.json", "a") as file:
    json.dump(computer, file, indent = 2)