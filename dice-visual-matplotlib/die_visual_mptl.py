import matplotlib.pyplot as plt

from die import Die


# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


x_values = list(range(1,7))

# Visualize the results.

# Set the size of the plotting window.
plt.figure(figsize=(10, 6))

hist = plt.bar(x_values, frequencies)

plt.title("Results of rolling one D6 1000 times.", fontsize=24)
plt.xlabel("Side Number", fontsize=14)
plt.ylabel("Number of Times Rolled", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()
