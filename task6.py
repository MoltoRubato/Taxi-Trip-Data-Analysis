from helper_functions import day_of_week, plot_label
import pandas as pd
import matplotlib.pyplot as plt

# The colour code for the days of the week
COLOURMAP = {'Monday': 'red', 'Tuesday': 'orange', 
             'Wednesday': 'yellow', 'Thursday': 'green', 
             'Friday': 'blue', 'Saturday': 'indigo', 'Sunday': 'violet'}
# The days of the week
WEEK = ['Monday', 'Tuesday', 'Wednesday', 
        'Thursday', 'Friday', 'Saturday', 'Sunday']

def task6():
    """Read in the relevant csv file. Find the day of the week (Sunday to 
    Saturday) on which the trip began, compute the mean trip distance and 
    mean total trip fare for each day of the week. Draw a scatter plot showing 
    mean trip distance (y axis) versus mean total amount for the 7 days of the 
    week. Output the scatter plot as a png file."""

    # First, we'll read in the csv file containing all trips records 
    # (since the task didnt specify January)
    trips_january = pd.read_csv('trips_january_duration.csv')

    # We'll create a new column for the day of the week each trip began on
    trips_january['dayofweek'] = None

    # We'll go through each trip record to check their start date
    for index, row in trips_january[['lpep_pickup_datetime']].iterrows():
        start_datetime = row['lpep_pickup_datetime']
        
        # Here, we'll assign each trip their day of the week
        trips_january.at[index, 'dayofweek'] = day_of_week(start_datetime)

    # For future use, we will save this new column to a seperate CSV file
    trips_january.to_csv('trips_january_dayofweek.csv', index=False)
    
    # Next, we'll create our scatterplot
    # We'll create a helper plotting dataframe with mean distance and fare
    plot_df = pd.DataFrame()
    mean_distance = []
    mean_fare = []

    # Here, we'll get the mean distance and fare for each day of the week
    for day in WEEK:
        each_day = trips_january.loc[trips_january['dayofweek']==day]

        mean_distance.append(each_day['trip_distance'].mean())
        mean_fare.append(each_day['total_amount'].mean())
        
    # Then, we will assemble the helper dataframe
    plot_df['Days'] = WEEK
    plot_df['Mean Distance'] = mean_distance
    plot_df['Mean Fare'] = mean_fare


    # Now, we will plot the points for each day of the week
    for index, row in plot_df.iterrows():
        # We'll map the colour and label depending on the day of the week
        plt.scatter(row['Mean Fare'], row['Mean Distance'], 
            label=row['Days'], c=COLOURMAP[row['Days']]) 
    
    # Adding a grid, plot labels, and legends
    plt.grid()
    plot_label('Mean total payment amount vs Mean trip distance', 
        'Mean total payment amount (dollars)', 'Mean trip distance (miles)')
    plt.legend() 

    # Finally, we can save the graph as a png
    plt.savefig('task6_scatter.png')
    plt.close()

    return
