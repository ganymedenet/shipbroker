import json

import requests
import brotli
import re


class Getter:
    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': "*/*",
        })

        self.result = dict()

    def get(self, url):
        link = "https://www.marinetraffic.com/getData/get_data_json_4/z:13/X:2079/Y:1594/station:0"

        res = self.session.get(url)

        print(res.status_code)
        print(res.content)

        compressed_data = res.content

        # decompressed_data = brotli.decompress(compressed_data)

        try:
            text = compressed_data.decode('utf-8')
            print(text)
        except UnicodeDecodeError:
            print("The decompressed data could not be decoded to UTF-8 text.")

        pattern = r'^(\d{1,2})\s+0\s+(\d{9}|\d{7})\s+([^\d\n]+?)\s+([\d.]+)\s+([\d.]+).*?(\d+)\s+(\w+)\s*$'

        # Use regex to parse each line
        parsed_data = re.findall(pattern, text, re.MULTILINE)
        #
        print(parsed_data)

        # readable_date = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        res = [
            dict(
                type=x[0],
                mmsi=x[1],
                name=x[2],
                eta=x[5],
                dest=x[6]
            )
            for x in parsed_data]

        print(json.dumps(res, indent=3))


if __name__ == "__main__":
    w = "https://www.marinetraffic.com/en/ais/get_info_window_json?asset_type=ship&id=407191"

    x = "https://www.vesselfinder.com/api/pub/click/352001737"

    url = "https://www.myshiptracking.com/requests/vesselsonmaptempTTT.php?type=json&minlat=34.25102911605338&maxlat=34.887183284717274&minlon=32.50683271013716&maxlon=33.405433042915355&zoom=10&selid=-1&seltype=0&timecode=-1&filters=%7B%22vtypes%22%3A%22%2C0%2C3%2C4%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%22%2C%22ports%22%3A%221%22%2C%22minsog%22%3A0%2C%22maxsog%22%3A60%2C%22minsz%22%3A0%2C%22maxsz%22%3A500%2C%22minyr%22%3A1950%2C%22maxyr%22%3A2024%2C%22status%22%3A%22%22%2C%22mapflt_from%22%3A%22%22%2C%22mapflt_dest%22%3A%22%22%7D"

    client = Getter()

    client.get(url)

    """
    type: json
    minlat: 34.3903917116532
    maxlat: 34.76614028694967
    minlon: 32.831593173607004
    maxlon: 33.3601297629607
    zoom: 11
    selid: -1
    seltype: 0
    timecode: -1
    filters: {"vtypes":",0,3,4,6,7,8,9,10,11,12,13","ports":"1","minsog":0,"maxsog":60,"minsz":0,"maxsz":500,"minyr":1950,"maxyr":2024,"status":"","mapflt_from":"","mapflt_dest":""}
    """
