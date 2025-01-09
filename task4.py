import pandas as pd
import datetime
from helper_functions import json_output, day_of_week

ROUND_TO = 2    # Rounding requirements        

def task4():
    """Read in the csv file containing only trips that occured in January. 
    Check whether a trip started on a weekday or weekend, calculate the 
    percentage of weekend trips then output the result percentage in a 
    json file"""

    # First, we'll read in the csv file only containing trips from January
    trips_in_january = pd.read_csv('trips_in_january.csv')

    # We'll create a new column to record if the trip took place on a weekend
    trips_in_january['isWeekend'] = 0
    weekend_count = 0

    # Next, we will check the pickup time of each trip for weekend trips
    for index, row in trips_in_january[['lpep_pickup_datetime']].iterrows():
        start_datetime = row['lpep_pickup_datetime']

        # We'll update the column to flag the day as a weekend
        if day_of_week(start_datetime) in ["Saturday", "Sunday"]: 
            trips_in_january.at[index, 'isWeekend'] = 1
            weekend_count += 1

    # Here, we will calculate the proportion of weekend trips as a percentage
    weekend_percent = round(weekend_count / len(trips_in_january) 
        * 100, ROUND_TO)

    # Lastly, we will output our findings to a json file
    results_dict = {"Percentage of weekend trips in January": weekend_percent}
    json_output(results_dict, "task4_summary.json")

    return
