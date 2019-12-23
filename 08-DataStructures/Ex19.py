import json

with open("euro.json") as file:
    data = json.load(file)
    
    print("Data:" + " " * 13 + "Kupno:" + " " * 13 + "Sprzedaż:")
    print("=" * 46)
    
    for x in data["rates"]:
        print(x["effectiveDate"] + " " * 8 + str(x["bid"]) + " " * 13 + str(x["ask"]))