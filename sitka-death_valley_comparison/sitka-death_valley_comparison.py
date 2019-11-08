from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from dataset import Dataset

# Create a dataset.
ds_1 = Dataset('data/death_valley_2014.csv')
ds_2 = Dataset('data/sitka_weather_2014.csv')

ds_1.extract_data()
ds_2.extract_data()


# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))

# Dataset 1
plt.plot(ds_1.dates, ds_1.highs, c='red', alpha=0.5)
plt.plot(ds_1.dates, ds_1.lows, c='blue', alpha=0.5)

# Dataset 2.
plt.plot(ds_2.dates, ds_2.highs, c='m', alpha=0.5)
plt.plot(ds_2.dates, ds_2.lows, c='c', alpha=0.5)


# Format plot.
title="Daily high and low temperatures - 2014\nDeath Valley, CA vs Sitka, AK"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Create legend.
red_patch = mpatches.Patch(color='red', label='MAX Death Valley')
magenta_patch = mpatches.Patch(color='m', label='MAX Sitka')
blue_patch = mpatches.Patch(color='blue', label='MIN Death Valley ')
cyan_patch = mpatches.Patch(color='c', label='MIN Sitka')
plt.legend(handles=[red_patch, magenta_patch, blue_patch, cyan_patch])


plt.show()