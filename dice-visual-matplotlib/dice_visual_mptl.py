import matplotlib.pyplot as plt

from die import Die


# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyze the results.
frequencies = []
min_result = die_1.num_of_die + die_2.num_of_die
max_result = die_1.num_sides + die_2.num_sides
for value in range(min_result, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results.
x_values = list(range(min_result, max_result+1))

# Set the size of the plotting window.
plt.figure(figsize=(10, 6))

hist = plt.bar(x_values, frequencies)

plt.title("Results of rolling two D6 1000 times.", fontsize=24)
plt.xlabel("Side Number", fontsize=14)
plt.ylabel("Number of Times Rolled", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()