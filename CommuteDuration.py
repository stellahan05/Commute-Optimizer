import googlemaps
from datetime import datetime

API_KEY = 'AIzaSyCm-4Mm_87c7XgJYeFYfdHw0DdGHb1AKOY'
gmaps = googlemaps.Client(key=API_KEY)

origin = '3109 161St, Surrey, BC, V3Z 2K4, Canada'
destination = '6115 Student Union Blvd, Vancouver, BC, V6T 2A1, Canada'

def get_route_info():
    now = datetime.now()
    directions_result = gmaps.directions(origin, destination, departure_time=now, mode='driving', traffic_model='best_guess')

    try:
        if directions_result:
            route = directions_result[0]['legs'][0]

            print(f"Duration in traffic: {route['duration_in_traffic']['text']}")
            print(f"Distance: {route['distance']['text']}")
        else:
            print("No results found.")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    get_route_info()