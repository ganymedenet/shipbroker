import json
import time
import httpx
import requests
import brotli
import re


class Getter:
    def __init__(self):
        self.cookies = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': "*/*",
            "Priority": "u=1, i",
            'Referer': "https://www.marinetraffic.com/en/ais/embed/zoom:3/centery:33.6/centerx:-95/maptype:3/shownames:true/mmsi:/shipid:0/fleet:/fleet_id:/vtypes:/showmenu:true/remember:true",
            "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125"',
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            # "Vessel-Image": "005a3f3dfcc8a9a1f6bf7e9fb457b3f1a629",
            "X-Kl-Kis-Ajax-Request": "Ajax_Request",
            "X-Newrelic-Id": "undefined",
            "X-Requested-With": "XMLHttpRequest"

        }

        self.result = dict()

    def get(self):
        with httpx.Client(cookies=self.cookies, follow_redirects=True) as client:

            url = "https://www.marinetraffic.com/en/ais/home/centerx:-12.0/centery:25.0/zoom:4"
            url = "https://www.marinetraffic.com/en/ais/home"
            # url = 'https://www.marinetraffic.com'

            url = "https://www.marinetraffic.com/en/ais/details/ships/shipid:5861209/mmsi:341961000/imo:9823871/vessel:UGAH_DISCOVERY"
            response = client.get(url)
            print(response.status_code)  # Print the status code to see the response
            print(response.text)


if __name__ == "__main__":
    client = Getter()

    client.get()
