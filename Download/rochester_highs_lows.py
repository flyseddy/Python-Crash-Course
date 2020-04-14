import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/rochester_weather_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # dates, highs, lows
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing value for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
title = "Daily Highs and Lows in Rochester"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
