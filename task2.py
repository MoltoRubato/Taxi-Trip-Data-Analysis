import pandas as pd
from helper_functions import json_output

NORMAL_LOWER = 0.1          # The lower value of the specified 'normal' range
NORMAL_UPPER = 17.3         # The upper value of the specified 'normal' range
ROUNDING = ".2f"            # Rounding requirements

def task2():
    """Read in the specified csv file. Compute the percentage of "abnormal"
    trip records in the data, then output the result rounded to 2 decimal 
    places in a json file"""

    # First, we'll read in the csv file
    trips_january = pd.read_csv('trips_january.csv')

    # Here, we'll find the abnormal distance records and their proportion
    abnormal_num = len(
        trips_january.loc[(trips_january['trip_distance'] > NORMAL_UPPER) |
                          (trips_january['trip_distance'] < NORMAL_LOWER)]
                          )
    abnormal_percent = format(abnormal_num/len(trips_january)*100, ROUNDING)

    # Lastly, we will output our findings to a json file
    results_dict = {
        "Percentage of abnormal trip distance records": abnormal_percent
        }
    json_output(results_dict, "task2_summary.json")

    return
