import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


# Load data
dataset = pd.read_csv('C:/filepath/Mean WVS + Econ by Country.csv')

# For Leisure
# Summary statistics
print(dataset['Mean_Q3'].describe())

# Number of bins
num_bins = 5

# Create the histogram
n, bins, patches = plt.hist(dataset['Mean_Q3'], bins=num_bins, density=1, alpha=0.7, color='blue', edgecolor='black')

# Calculate the bin width
bin_width = bins[1] - bins[0]

# Convert histogram to percentages
n_percent = n * bin_width * 100  # Now the sum(n_percent * bin_width) should be 100

# Update histogram y-values to percentages
for i in range(num_bins):
    patches[i].set_height(n_percent[i])

plt.ylim(0, max(n_percent) * 1.1)  # Update y-limit to match new heights

# Mean and standard deviation of the dataset
mu, std = dataset['Mean_Q3'].mean(), dataset['Mean_Q3'].std()

# Create an array of x values to plot the fit
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Generate the y-values for the normal distribution
y = norm.pdf(x, mu, std)

# Scale the y-values (in density, so that the area under the curve is 1)
y = y * bin_width  # Scale by bin_width to match the histogram

# Convert density y-values to percentages
y_percent = y * 100  # Now the area under the curve should be 100

# Plot the scaled density curve
plt.plot(x, y_percent, 'k', linewidth=2)

# Add title and labels
plt.title('Fitted normal distribution')
plt.xlabel('Leisure')
plt.ylabel('Percentage %')

# Show the plot
plt.show()



# For Trust
# Summary statistics
print(dataset['Mean_Q61'].describe())

# Number of bins
num_bins = 5

# Create the histogram
n, bins, patches = plt.hist(dataset['Mean_Q61'], bins=num_bins, density=1, alpha=0.7, color='g', edgecolor='black')

# Calculate the bin width
bin_width = bins[1] - bins[0]

# Convert histogram to percentages
n_percent = n * bin_width * 100  # Now the sum(n_percent * bin_width) should be 100

# Update histogram y-values to percentages
for i in range(num_bins):
    patches[i].set_height(n_percent[i])

plt.ylim(0, max(n_percent) * 1.1)  # Update y-limit to match new heights

# Mean and standard deviation of the dataset
mu, std = dataset['Mean_Q61'].mean(), dataset['Mean_Q61'].std()

# Create an array of x values to plot the fit
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Generate the y-values for the normal distribution
y = norm.pdf(x, mu, std)

# Scale the y-values (in density, so that the area under the curve is 1)
y = y * bin_width  # Scale by bin_width to match the histogram

# Convert density y-values to percentages
y_percent = y * 100  # Now the area under the curve should be 100

# Plot the scaled density curve
plt.plot(x, y_percent, 'k', linewidth=2)

# Add title and labels
plt.title('Fitted normal distribution')
plt.xlabel('Trust')
plt.ylabel('Percentage %')

# Show the plot
plt.show()


# For Moral Relativism
# Summary statistics
print(dataset['Mean_Q176'].describe())

# Number of bins
num_bins = 5

# Create the histogram
n, bins, patches = plt.hist(dataset['Mean_Q176'], bins=num_bins, density=1, alpha=0.7, color='orange', edgecolor='black')

# Calculate the bin width
bin_width = bins[1] - bins[0]

# Convert histogram to percentages
n_percent = n * bin_width * 100  # Now the sum(n_percent * bin_width) should be 100

# Update histogram y-values to percentages
for i in range(num_bins):
    patches[i].set_height(n_percent[i])

plt.ylim(0, max(n_percent) * 1.1)  # Update y-limit to match new heights

# Mean and standard deviation of the dataset
mu, std = dataset['Mean_Q176'].mean(), dataset['Mean_Q176'].std()

# Create an array of x values to plot the fit
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Generate the y-values for the normal distribution
y = norm.pdf(x, mu, std)

# Scale the y-values (in density, so that the area under the curve is 1)
y = y * bin_width  # Scale by bin_width to match the histogram

# Convert density y-values to percentages
y_percent = y * 100  # Now the area under the curve should be 100

# Plot the scaled density curve
plt.plot(x, y_percent, 'k', linewidth=2)

# Add title and labels
plt.title('Fitted normal distribution')
plt.xlabel('Moral relativism')
plt.ylabel('Percentage %')

# Show the plot
plt.show()
