
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


## For Leisure
# Load dataset
dataset = pd.read_csv('C:/filepath/Mean WVS + Econ by Country.csv')

# Summary statistics
dataset['Mean_Q3'].describe()


# Create the histogram with percentage on the y-axis
# Manually setting bin edges
# Note: if not setting bin edges manually, bin = 10 (or any other desirable number)

bin_edges = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]

# Calculate the weights for each bin
weights = np.ones_like(dataset['Mean_Q3']) / len(dataset['Mean_Q3']) * 100


n, bins, patches = plt.hist(dataset['Mean_Q3'], bins=bin_edges, edgecolor='black', weights=weights)

# Calculate bin size
bin_size = bins[1] - bins[0]
print(f'Bin size: {bin_size}')

# Annotate the bars with the specific percentage
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2., patches[i].get_height(),
             '{:1.0f}%'.format(n[i]),
             ha='center', va='bottom')

plt.title('Distribution of "Perception of Leisure"')
plt.xlabel('Perception of Leisure')
plt.ylabel('Percentage (%)')
plt.show()



## For Trust
# Summary statistics
dataset['Mean_Q61'].describe()


# Create the histogram with percentage on the y-axis
# Manually setting bin edges
bin_edges = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8]

# Calculate the weights for each bin
weights = np.ones_like(dataset['Mean_Q61']) / len(dataset['Mean_Q61']) * 100


n, bins, patches = plt.hist(dataset['Mean_Q61'], bins=bin_edges, edgecolor='black', weights=weights)

# Calculate bin size
bin_size = bins[1] - bins[0]
print(f'Bin size: {bin_size}')

# Annotate the bars with the specific percentage
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2., patches[i].get_height(),
             '{:1.0f}%'.format(n[i]),
             ha='center', va='bottom')
    
plt.title('Distribution of "Trust of new acquaintances"')
plt.xlabel('Trust of new acquaintances')
plt.ylabel('Percentage (%)')
plt.show()



## For Moral Relativism
# Summary statistics
dataset['Mean_Q176'].describe()

bin_edges = [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]

# Calculate the weights for each bin
weights = np.ones_like(dataset['Mean_Q176']) / len(dataset['Mean_Q176']) * 100

n, bins, patches = plt.hist(dataset['Mean_Q176'], bins=bin_edges, edgecolor='black', weights=weights)

# Calculate bin size
bin_size = bins[1] - bins[0]
print(f'Bin size: {bin_size}')

# Annotate the bars with the specific percentage
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2., patches[i].get_height(),
             '{:1.0f}%'.format(n[i]),
             ha='center', va='bottom')
    
plt.title('Distribution of Moral relativism')
plt.xlabel('Moral relativism')
plt.ylabel('Percentage (%)')
plt.show()
