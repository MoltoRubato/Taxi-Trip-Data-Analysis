import pandas as pd
import matplotlib.pyplot as plt

# The colour code for the days of the week
colours = ['red','orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# The days of the week
WEEK = ['Monday', 'Tuesday', 'Wednesday', 
        'Thursday', 'Friday', 'Saturday', 'Sunday']

def task7():
    """Read in the relevant csv file. Create a colour-coded pie chart showing 
    the mean trip duration for each day of the week. Output the pie chart in a 
    png file."""

    # First, we'll read in the csv file with assigned day of the week
    trips_january = pd.read_csv('trips_january_dayofweek.csv')

    # We'll find and record the mean trip duration for each day of the week
    mean_duration = []

    for day in WEEK:
        each_day = trips_january.loc[trips_january['dayofweek']==day]
        mean_duration.append(each_day['trip_duration'].mean())

    # Now, we will plot the colour-coded pie chart for each day of the week
    plt.pie(mean_duration, labels=WEEK, colors=colours, autopct='%1.1f%%')       

    # We'll add a title to the piechart
    plt.title("Mean trip duration for each day of the week")

    # Finally, we can save the graph as a png
    plt.savefig('task7_pie.png')
    plt.close()

    return
