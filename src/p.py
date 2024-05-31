import json
import re



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
file_path = './mp2'

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
