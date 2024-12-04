# -*- coding: utf-8 -*-

"""
past_analysis_script.py- Analyzes the performance of drivers at a specified circuit.  
"""

__author__ = "Austin Lopez"
__version__ = "1.2"
__email__ = "lopezaj88@gmail.com"
__status__ = "Testing"

import fastf1 as ff1
from fastf1 import plotting
import matplotlib.pyplot as plt

# Enable cache for FastF1 to speed up future data retrievals
#ff1.Cache.enable_cache('f1_cache')  # Specify a directory for caching data

def fetch_race_data(year, grand_prix):
    try:
        # Load the session data
        race = ff1.get_session(year, grand_prix, 'R')  
        race.load()
        
        # Create a list of drivers
        driverNumbers = race.drivers
        drivers = [race.get_driver(number)['Abbreviation'] for number in driverNumbers]
        
        # Summary of results
        print("\n--- Race Results ---")
        for driver in drivers:
            driverName = race.get_driver(driver)['FullName']
            teamName = race.get_driver(driver)['TeamName']
            position = race.get_driver(driver)['Position']
            status = race.get_driver(driver)['Status']
            points = race.get_driver(driver)['Points']
            
            print(f'Driver: {driverName} | Team: {teamName} | Position: {position} | Status: {status} | Points: | {points}')


        # Scoring Points
        print("\n--- Points Scored ---")
        for driver in drivers:
            scoring = race.get_driver(driver)['Points']
            if scoring > 0:
                print(f'Driver {driver} | Points {scoring}')
                

        # Non-scoring Drivers
        print("\n--- Non-scoring Drivers ---")
        non_scoring = [res for res in race.results if res['Points'] == 0]
        for driver in non_scoring:
            print(driver['FullName'])

        # Fastest Driver
        fastest_driver = race.laps.pick_fastest()
        print(f"\nFastest Lap: {fastest_driver['Driver']} with a lap time of {fastest_driver['LapTime']}")
        print("Fastest lap details:")
        print(fastest_driver)

        # Check if the fastest lap was influenced by a pit stop
        fastest_driver_pit = race.laps[race.laps['Driver'] == fastest_driver['Driver']]
        if not fastest_driver_pit.empty:
            pit_stops = fastest_driver_pit['PitInLap'].unique()
            print(f"{fastest_driver['Driver']} pit stops sequence: { pit_stops }")
        
        # Weather data
        print("\n--- Weather Data ---")
        weather = race.weather_data
        for time, data in weather.iterrows():
            print(f"Time: {time} | Air Temp: {data['AirTemp']}°C | Track Temp: {data['TrackTemp']}°C | Humidity: {data['Humidity']}% | Wind: {data['WindSpeed']} m/s, {data['WindDirection']}° | Rainfall: {data['Rainfall']} mm")

        # Race events
        print("\n--- Race Events ---")
        events = race.event_data
        for event in events:
            print(f"Time: {event['Time']} | Event: {event['Event']}")

        # Count specific events
        yellow_flags = [e for e in events if 'Yellow Flag' in e['Event']]
        red_flags = [e for e in events if 'Red Flag' in e['Event']]
        safety_cars = [e for e in events if 'Safety Car' in e['Event']]
        virtual_safety_cars = [e for e in events if 'Virtual Safety Car' in e['Event']]
        restarts = [e for e in events if 'Restart' in e['Event']]

        print(f"\nYellow Flags: {len(yellow_flags)}")
        print(f"Red Flags: {len(red_flags)}")
        print(f"Safety Cars: {len(safety_cars)}")
        print(f"Virtual Safety Cars: {len(virtual_safety_cars)}")
        print(f"Restarts: {len(restarts)}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_race_data(2024, 'Qatar')  

