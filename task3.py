import pandas as pd
import matplotlib.pyplot as plt
import datetime

DATETIME_FORMAT = '%d/%m/%Y %H:%M'  # Format of datetime used in the file 
MORNING_START = 7       # The specified start time of the morning period
MORNING_END = 11        # The specified end time of the morning period
AFTERNOON_START = 12    # The specified start time of the afternoon period
AFTERNOON_END = 15      # The specified end time of the afternoon period


def task3():
    """Read in the specified csv file. Plot 2 boxplots on one page to show 
    the distribution of trip fares during the morning and afternoon period. 
    The output is the full plot in a png file."""

    # First, we'll read in the csv file
    trips_january = pd.read_csv('trips_january.csv')

    # Initialise variables for morning and afternoon trip fare records
    morning_trips = []
    afternoon_trips = []

    # Select only the relevant columns to iterate through for efficiency
    selected_columns = trips_january[[
        'lpep_pickup_datetime', 'total_amount']]

    # Next, we will sort each trip record as morning or afternoon
    for index, row in selected_columns.iterrows():
        start_datetime = row['lpep_pickup_datetime']
        trip_fare = row['total_amount']
        start_time = datetime.datetime.strptime(start_datetime,
                                                DATETIME_FORMAT).time()

        # We will place each trip fare in their respective time groups
        if (datetime.time(MORNING_START, 0) <= start_time 
            <= datetime.time(MORNING_END, 0)):
            morning_trips.append(trip_fare)
        elif (datetime.time(AFTERNOON_START, 0) <= start_time 
            <= datetime.time(AFTERNOON_END, 0)):
            afternoon_trips.append(trip_fare)

    # Calculate the overall y-axis limits for both datasets  
    overall_min = min(min(morning_trips), min(afternoon_trips))
    overall_max = max(max(morning_trips), max(afternoon_trips))

    # Next, we will plot 2 side-by-side plots
    fig, (ax1, ax2) = plt.subplots(1, 2) 

    # We'll name the plot
    fig.suptitle('Distribution of trip fares (dollars)') 

    # Here, we will draw the first box plot
    ax1.boxplot(morning_trips) 
    ax1.set_title('Morning Trips')
    ax1.set_ylim(overall_min, overall_max)

    # Here, we will draw the second box plot
    ax2.boxplot(afternoon_trips) 
    ax2.set_title('Afternoon Trips')
    ax2.set_ylim(overall_min, overall_max)

    # Lastly, we'll save the graph as a png
    plt.savefig('task3_boxplot.png') 
    plt.close() 

    return
