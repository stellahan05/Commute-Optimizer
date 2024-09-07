import csv
import googlemaps
from datetime import datetime

API_KEY = 'AIzaSyCm-4Mm_87c7XgJYeFYfdHw0DdGHb1AKOY'
gmaps = googlemaps.Client(key=API_KEY)

origin = '3109 161St, Surrey, BC, V3Z 2K4, Canada'
destination = '6115 Student Union Blvd, Vancouver, BC, V6T 2A1, Canada'

def get_route_info():
    now = datetime.now()
    directions_result = gmaps.directions(origin, destination, departure_time=now, mode='driving', traffic_model='best_guess')

    if directions_result:
        route = directions_result[0]['legs'][0]
        duration = route['duration_in_traffic']['text']
        distance = route['distance']['text']
        
        # Append data to CSV
        with open('traffic_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['timestamp', 'duration_in_traffic', 'distance']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()
                
            writer.writerow({
                'timestamp': now.strftime('%Y-%m-%d %H:%M:%S'),
                'duration_in_traffic': duration,
                'distance': distance
            })

    else:
        print("No results found.")