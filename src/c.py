import pyproj

# Define the projection transformation (Web Mercator to WGS84)
transformer = pyproj.Transformer.from_crs("EPSG:3857", "EPSG:4326")

# Bounding box coordinates in Web Mercator (meters)
minX, minY = -242010, 21551036
maxX, maxY = 28167, 21713860

# Convert min coordinates
min_lat, min_lon = transformer.transform(minY, minX)
# Convert max coordinates
max_lat, max_lon = transformer.transform(maxY, maxX)

print(f"Min Coordinates: Latitude={min_lat}, Longitude={min_lon}")
print(f"Max Coordinates: Latitude={max_lat}, Longitude={max_lon}")
