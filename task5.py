import pandas as pd
import matplotlib.pyplot as plt
import datetime
from helper_functions import day_of_week, plot_label


BIN_EDGES = [0, 7, 9, 12, 16, 20, 24]   # Specified hour ranges
DATETIME_FORMAT = '%d/%m/%Y %H:%M'  # Format of datetime used in the file 

def task5():
    """Read in the specified csv file. Find the hour in which the trip began, 
    plot two histograms showing the frequency of taxi trips over hours of the 
    day. One histogram for weekends and one histogram for weekdays. Output the 
    histograms as two png files."""

    # First, we'll read in the original csv file (task didnt specify January)
    trips_january = pd.read_csv('trips_january.csv')

    # We'll create new columns to record the pick-up hour of the trip
    trips_january['Hour'] = None
    # And a new column for if the day is a weekend
    trips_january['isWeekend'] = 0

    # Next, we will sort each trip record as morning or afternoon
    for index, row in trips_january[['lpep_pickup_datetime']].iterrows():
        start_datetime = row['lpep_pickup_datetime']

        # We'll update the column to flag the day as a weekend
        if day_of_week(start_datetime) in ["Saturday", "Sunday"]: 
            trips_january.at[index, 'isWeekend'] = 1

        # We'll also get the hour number
        start_time = datetime.datetime.strptime(start_datetime, 
            DATETIME_FORMAT).time()
        trips_january.at[index, 'Hour'] = start_time.hour

    # Next, we'll create the histograms for weekends
    plt.hist(trips_january.loc[trips_january['isWeekend'] == 1]['Hour'],
        bins=BIN_EDGES, edgecolor='black')

    # Here we'll add labels, title, and display custom bin edges
    plot_label('Frequency of taxi trips over hours of the day on Weekends', 
        'Hours', 'Frequency')
    plt.xticks(BIN_EDGES)
    plt.xlim(BIN_EDGES[0], BIN_EDGES[-1])

    # Then, we can save the graph as a png
    plt.savefig('task5_histogram_weekend.png')
    plt.close()

    # Next, we'll create the histograms for weekdays
    plt.hist(trips_january.loc[trips_january['isWeekend'] == 0]['Hour'], 
        bins=BIN_EDGES, edgecolor='black')

    # Here we'll add labels, title, and display custom bin edges
    plot_label('Frequency of taxi trips over hours of the day on Weekdays',
        'Hours', 'Frequency')

    plt.xticks(BIN_EDGES)
    plt.xlim(BIN_EDGES[0], BIN_EDGES[-1])

    # Finally, we can save the graph as a png
    plt.savefig('task5_histogram_weekday.png')
    plt.close()

    return
