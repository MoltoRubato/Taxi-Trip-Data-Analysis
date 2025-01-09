# EODP_Project1 - Taxi Trip Data Analysis

This project analyses taxi trip data using Python's `pandas`, `matplotlib`, and `re` libraries. The dataset used consists of taxi trips data from January, stored in a CSV file, and the goal is to extract insights, visualize patterns, and evaluate data quality.

## Tasks Overview

### Task 1: Loading Data and Adding a Column
- **Objective**: Load the `trips_january.csv` file into a pandas DataFrame, compute the duration of each trip, and add this as a new column `trip_duration`. Output the number of records and the mean trip duration in a JSON file.
- **Command**: `python main.py task1`

### Task 2: Data Quality
- **Objective**: Identify abnormal trip distances (values not in the range [0.1, 17.3]) and compute their percentage.
- **Command**: `python main.py task2`

### Task 3: Data Visualization using Boxplots
- **Objective**: Create two boxplots comparing trip fares for the morning (07:00 - 11:00) and afternoon (12:00 - 15:00) periods. Output a PNG file of the boxplots.
- **Command**: `python main.py task3`

### Task 4: Days of the Week Behaviour
- **Objective**: Add a column `isWeekend` to the DataFrame to mark weekends (1) and weekdays (0), then calculate the percentage of weekend trips.
- **Command**: `python main.py task4`

### Task 5: Hourly Behaviour
- **Objective**: Add a column `hour` indicating the hour the trip started, then generate two histograms showing the frequency of taxi trips over the hours of the day, one for weekends and one for weekdays.
- **Command**: `python main.py task5`

### Task 6: Scatter Plot
- **Objective**: Compute and plot a scatter plot showing the mean trip distance vs. the mean total amount for each day of the week. Each day should be plotted in a different color.
- **Command**: `python main.py task6`

### Task 7: Pie Chart
- **Objective**: Create a pie chart representing the mean trip duration for each day of the week, with percentage values and day labels.
- **Command**: `python main.py task7`

## Installation and Requirements

1. Install dependencies:

```bash
pip install pandas matplotlib
```
2. Clone the repository:

```bash
git clone https://github.com/yourusername/taxi-trip-analysis.git
cd taxi-trip-analysis
```

Usage
For each task, run the corresponding command from the terminal:

```bash
python main.py task1
python main.py task2
python main.py task3
python main.py task4
python main.py task5
python main.py task6
python main.py task7
```
Outputs
```
Task 1: task1_summary.json
Task 2: task2_summary.json
Task 3: task3_boxplot.png
Task 4: task4_summary.json
Task 5: task5_histogram_weekend.png, task5_histogram_weekday.png
Task 6: task6_scatter.png
Task 7: task7_pie.png
```

## Tools used  
- Python
- pandas, re, matplotlib 

## Contributors
- Ryan Huang
- University of Melbourne COMP20008 Teaching Team (Helper function and question provider)

## License
This project is for academic purposes under the University of Melbourne's COMP20008 course



