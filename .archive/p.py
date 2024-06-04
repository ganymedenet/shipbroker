import json
import re

w = "https://www.marinetraffic.com/en/ais/get_info_window_json?asset_type=ship&id=407191"

x = "https://www.vesselfinder.com/api/pub/click/352001737"

url = "https://www.myshiptracking.com/requests/vesselsonmaptempTTT.php?type=json&minlat=34.25102911605338&maxlat=34.887183284717274&minlon=32.50683271013716&maxlon=33.405433042915355&zoom=10&selid=-1&seltype=0&timecode=-1&filters=%7B%22vtypes%22%3A%22%2C0%2C3%2C4%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%22%2C%22ports%22%3A%221%22%2C%22minsog%22%3A0%2C%22maxsog%22%3A60%2C%22minsz%22%3A0%2C%22maxsz%22%3A500%2C%22minyr%22%3A1950%2C%22maxyr%22%3A2024%2C%22status%22%3A%22%22%2C%22mapflt_from%22%3A%22%22%2C%22mapflt_dest%22%3A%22%22%7D"


def get(self, url):
    # link = "https://www.marinetraffic.com/getData/get_data_json_4/z:13/X:2079/Y:1594/station:0"

    # minlat = 34.25102911605338
    # maxlat = 34.887183284717274
    # minlon = 32.50683271013716
    # maxlon = 33.405433042915355

    minlat = 34.25102911605338
    maxlat = 34.887183284717274
    minlon = 32.50683271013716
    maxlon = 33.405433042915355

    params = {
        "type": "json",
        "minlat": minlat,
        "maxlat": maxlat,
        "minlon": minlon,
        "maxlon": maxlon,
        "zoom": 11,
        "selid": -1,
        "seltype": 0,
        "timecode": -1,
        "filters": {
            "vtypes": ",0,3,4,6,7,8,9,10,11,12,13",
            "ports": "1",
            "minsog": 0,
            "maxsog": 60,
            "minsz": 0,
            "maxsz": 500,
            "minyr": 1950,
            "maxyr": 2024,
            "status": "",
            "mapflt_from": "",
            "mapflt_dest": ""
        }

    }

    url = "https://www.myshiptracking.com/requests/vesselsonmaptempTTT.php"

    res = self.session.get(url, params=params)

    # print(res.status_code)
    # print(res.content)

    compressed_data = res.content

    # decompressed_data = brotli.decompress(compressed_data)
    response = compressed_data.decode('utf-8')
    # try:
    #     text = compressed_data.decode('utf-8')
    #     print(text)
    # except UnicodeDecodeError:
    #     print("The decompressed data could not be decoded to UTF-8 text.")

    res = self.parse(response)
    print(json.dumps(res, indent=3))


@staticmethod
def parse(response):
    pattern = r'^(\d{1,2})\s+0\s+(\d{9}|\d{7})\s+([^\d\n]+?)\s+([\d.]+)\s+([\d.]+).*?(\d+)\s+(\w+)\s*$'

    # Use regex to parse each line
    parsed_data = re.findall(pattern, response, re.MULTILINE)
    #
    # print(parsed_data)

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

    return res



def parse_ship_records(file_path):
    # Read the binary file content
    with open(file_path, 'rb') as file:
        data = file.read()

    # Define a regex pattern to match uppercase letters, numbers, and spaces (common in ship names)
    pattern = re.compile(b'[A-Z0-9 ]{3,}')

    records = []
    index = 0
    record_length = 60  # Initial assumption, may adjust based on actual data

    while index < len(data):
        record = data[index:index + record_length]

        # Extract ship name using regex pattern
        ship_name_matches = pattern.findall(record)
        ship_name = ship_name_matches[0].decode('ascii', errors='ignore').strip() if ship_name_matches else ""

        # Extract coordinates (adjusting offsets as needed)
        coord_start = 5
        coord_length = 10
        coordinates = record[coord_start:coord_start + coord_length].hex()

        ship_info = {
            "ship_name": ship_name,
            "coordinates": coordinates,
            "raw_record": record.hex()
        }
        records.append(ship_info)
        index += record_length

    return records


# Path to the binary file
file_path = '../src/mp2'

# Parse the ship records from the file content
ship_records = parse_ship_records(file_path)

print(json.dumps(ship_records, indent=3))
# Convert to a DataFrame for better readability
# ship_records_df = pd.DataFrame(ship_records)
#
# # Save the DataFrame to a CSV file for further analysis
# ship_records_df.to_csv('parsed_ship_records.csv', index=False)
#
# # Display the DataFrame
# print(ship_records_df.head())
