import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt

TAB_INDENT = 4    
SECONDS_IN_MIN = 60                  
DATETIME_FORMAT = '%d/%m/%Y %H:%M'      # Format of datetime used in the file 
QUOTIENT = 0                        # Index of quotient in the divmod() output

def json_output(input_dictionary,output_name):
    """Takes a dictionary as input. Exports the dictionary to a json file
    Nothing is returned."""

    # write dataframe in the new output json file
    out_json = open(output_name, "w") 
    json.dump(input_dictionary, out_json, indent = TAB_INDENT) 
    out_json.close() 

    return


def day_of_week(date_time):
    """Takes in a datetime string. Following the format of datetime used 
    in the task, returns the day of the week."""

    day = datetime.datetime.strptime(date_time, 
            DATETIME_FORMAT).date().weekday()

    # from the datetime we'll return the correct day of the week 
    match day:
        case 0:
            return 'Monday'
        case 1:
            return 'Tuesday'
        case 2:
            return 'Wednesday'
        case 3:
            return 'Thursday'
        case 4:
            return 'Friday'
        case 5:
            return 'Saturday'
        case 6:
            return 'Sunday'

    return


def duration_mins(start, end):
    """Takes in a starting and an ending datetime string, calculate 
    their difference to find and return the duration of the event 
    in minutes. Including minutes as the lowest unit"""

    #finding the difference between pickup and dropoff for duration
    duration = pd.to_datetime(end, dayfirst=True) - pd.to_datetime(start, 
        dayfirst=True)
    return (divmod(duration.total_seconds(), SECONDS_IN_MIN)[QUOTIENT])


def plot_label(plot_title, x_label, y_label):
    """Takes in string values for a plots title, X axis and Y axis labels.
    Apply them to the current opened plot. Nothing is returned."""
    
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    return 








