import time

import requests
import json

api = "5b9f834b-0592-4663-96a0-b86c8465db85"

# params = {
#     'api-key': api,
#     'mmsi': '273358260'
# }
# method = 'vessel'
# api_base = 'https://api.datalastic.com/api/v0/'
# api_result = requests.get(api_base + method, params)
# api_response = api_result.json()

url = "https://api.datalastic.com/api/v0/vessel_inradius"

# 46.00895917585131, 36.26037252919501
points = [
    (45.0, 36.0),
    (45.0, 36.45),
    (45.0, 36.9),
    (45.0, 37.35),
    (45.0, 37.8),
    (45.0, 38.25),
    (45.0, 38.7),
    (45.45, 36.0),
    (45.45, 36.45),
    (45.45, 36.9),
    (45.45, 37.35),
    (45.45, 37.8),
    (45.45, 38.25),
    (45.45, 38.7),
    (45.9, 36.0),
    (45.9, 36.45),
    (45.9, 36.9),
    (45.9, 37.35),
    (45.9, 37.8),
    (45.9, 38.25),
    (45.9, 38.7),
    (46.35, 36.0),
    (46.35, 36.45),
    (46.35, 36.9),
    (46.35, 37.35),
    (46.35, 37.8),
    (46.35, 38.25),
    (46.35, 38.7),
    (46.8, 36.0),
    (46.8, 36.45),
    (46.8, 36.9),
    (46.8, 37.35),
    (46.8, 37.8),
    (46.8, 38.25),
    (46.8, 38.7),
    (47.25, 36.0),
    (47.25, 36.45),
    (47.25, 36.9),
    (47.25, 37.35),
    (47.25, 37.8),
    (47.25, 38.25),
    (47.25, 38.7),
]

result = []

for loc in points:
    params = {
        'api-key': api,
        "lat": loc[0],
        "lon": loc[1],
        "radius": 50,
        "type": "cargo"
    }

    api_response = requests.get(url, params=params).json()

    # print(json.dumps(api_response, indent=4, sort_keys=True))
    #
    # print()
    for vessel in api_response["data"]["vessels"]:
        if vessel not in result:
            result.append(vessel)

    print(len(api_response["data"]["vessels"]))
    time.sleep(1)

print("Total", len(result))

with open("../src/res.json", "w") as file:
    file.write(json.dumps(result, indent=3))


