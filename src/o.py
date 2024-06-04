from zenrows import ZenRowsClient

client = ZenRowsClient("0cf1d8572244c5ef0a5f29d18fe465a49514763f")
url = "https://opensea.io/rankings/trending"

url = "https://www.marinetraffic.com/en/ais/home"
url = "https://www.marinetraffic.com/en/ais/home/centerx:-12.0/centery:25.0/zoom:4"

# url = "https://www.marinetraffic.com/getData/get_data_json_4/z:8/X:77/Y:46/station:0"

# url = "https://www.marinetraffic.com/en/ais/home"

url = "https://www.marinetraffic.com/en/ais/details/ships/shipid:5861209/mmsi:341961000/imo:9823871/vessel:UGAH_DISCOVERY"

# ulr= "https://www.marinetraffic.com/en/vessels/348769/voyage"

params = {
    "js_render": "true",
    "json_response": "true"
}

response = client.get(url)

print(response.status_code)
print(response.text)

with open("test.html", "w", encoding='utf-8') as file:
    file.write(response.text)
