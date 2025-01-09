import pandas as pd
import re 
from helper_functions import json_output, duration_mins


DATE_FORMAT = '([1-9]|[12][0-9]|3[01])/1/\d{4}' # January-only date Format
ROUNDING = ".2f"                                # Rounding requirements

def task1():
    """Read in the specified csv file. Compute and record the duration of 
    every trip in minutes in a new column 'trip_duration'. Find the number 
    of trips records and the mean trip duration for trips that specifically 
    occured in January, and output this in a json file"""
    
    # First, we'll read in the csv file
    trips_january = pd.read_csv('trips_january.csv')
    # We'll create a seperate dataframe for trips that truly began in January
    trips_in_january = trips_january.copy()

    # Initialise variables that record the trip durations sum
    duration_sum = 0
    # We'll create a new column for the trip duration
    trips_january['trip_duration'] = None

    # Select only the relevant columns to iterate through for efficiency
    selected_columns = trips_january[[
        'lpep_pickup_datetime', 'lpep_dropoff_datetime']]


    # Next, we'll go through each recorded trip to find their duration
    for index, row in selected_columns.iterrows():

        # We will extract the trip's start and end datetime
        pickup_datetime = row['lpep_pickup_datetime']
        dropoff_datetime = row['lpep_dropoff_datetime']

        # Then we'll find the trip duration using the datetime difference
        duration_in_mins = duration_mins(pickup_datetime, dropoff_datetime)

        # task1 requires us to record all trip durations in a new column
        trips_january.at[index, 'trip_duration'] = duration_mins(
            pickup_datetime, dropoff_datetime)
        
        # task1 requires only trips starting in January for the mean duration
        if re.search(DATE_FORMAT, pickup_datetime):
            duration_sum += duration_in_mins
        else: 
            trips_in_january = trips_in_january.drop(index)


    # For future use, we'll save only the January trips to a seperate CSV file
    trips_in_january.to_csv('trips_in_january.csv', index=False)
    
    # And for future use, we'll save all trip durations to a new file 
    trips_january.to_csv('trips_january_duration.csv', index=False)

    # Finally, we'll find the January-only record and the mean trip duration
    record_num = len(trips_in_january)
    mean_duration = format(duration_sum/record_num, ROUNDING)

    # Lastly, we will output our findings to a json file
    results_dict = {"Number of records in January": record_num,
                    "Mean trip duration in January": mean_duration}
    json_output(results_dict, "task1_summary.json")

    return
