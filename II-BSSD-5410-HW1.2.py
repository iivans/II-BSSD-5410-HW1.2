import requests
import math

URL_PATH = "https://nominatim.openstreetmap.org/search"

# THIS GETS LOCATION
def get_lat_lon(location):
    PARAMS = {'q': location, 'format': 'jsonv2'}
    headers = {'User-Agent': 'DistanceCalc/1.0'}
    response = requests.get(URL_PATH, params=PARAMS, headers=headers)
    data = response.json()
    return [float(data[0]['lat']), float(data[0]['lon'])]

# THIS CALCULATES DISTANCE 
def calculate_distance(lat1, lon1, lat2, lon2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (math.sin(dlat/2))**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin(dlon/2))**2
    a = min(1, max(0, a))  # Clamp a to be within the range [0, 1]
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = 3961 * c  # Radius of Earth in miles
    return d

# THIS SORTS 
def selection_sort(array, names):
    for currentIndex in range(len(array) - 1):
        minIndex = currentIndex
        for i in range(currentIndex + 1, len(array)):
            if array[i] < array[minIndex]:
                minIndex = i
        if minIndex != currentIndex:
            array[currentIndex], array[minIndex] = array[minIndex], array[currentIndex]
            names[currentIndex], names[minIndex] = names[minIndex], names[currentIndex]

def main():
    origin = "New Mexico Museum of Natural History & Science"
    destinations = [
        "University of New Mexico",
        "New Mexico State University",
        "New Mexico Highlands University",
        "Eastern New Mexico University",
        "Western New Mexico University"
    ]
    
    origin_coords = get_lat_lon(origin)
    distances = []
    names = []
    
    for place in destinations:
        coords = get_lat_lon(place)
        distance = calculate_distance(origin_coords[0], origin_coords[1], coords[0], coords[1])
        distances.append(distance)
        names.append(place)
    
    selection_sort(distances, names)
    
    print("Locations sorted by distance from the New Mexico Museum of Natural History & Science:")
    for name in names:
        print(name)

if __name__ == "__main__":
    main()