import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load data
dataset = pd.read_csv('C:/filepath/Mean WVS + Econ by Country.csv')


## Leisure
# Group by Mean_incomeWB and calculate relevant statistics for Mean_Q3
grouped = dataset.groupby('Mean_incomeWB')['Mean_Q3']

# Initialize empty DataFrame to store final results
result = pd.DataFrame()

# Calculate mean, standard deviation, and sample size for each group
result['mean'] = grouped.mean()
result['std_dev'] = grouped.std()
result['sample_size'] = grouped.count()

# Calculate standard error
result['std_err'] = result['std_dev'] / np.sqrt(result['sample_size'])

# Calculate 95% confidence intervals
result['lower_95'] = result['mean'] - 1.96 * result['std_err']
result['upper_95'] = result['mean'] + 1.96 * result['std_err']

# Format to 4 decimal places
result = result.round(4)

# Map Mean_incomeWB numbers to categories
result.index = result.index.map({1: 'Low', 2: 'Lower-middle', 3: 'Upper-middle', 4: 'High'})

# Plotting DataFrame as an image
fig, ax = plt.subplots(figsize=(12, 4))  # set the size that you'd like (width, height)
ax.axis('tight')
ax.axis('off')
plt.title("Leisure by Income group")
ax.table(cellText=result.values,
         colLabels=result.columns,
         rowLabels=result.index,
         cellLoc='center', loc='center')

plt.show()



## Trust
# Group by Mean_incomeWB and calculate relevant statistics for Mean_Q3
grouped = dataset.groupby('Mean_incomeWB')['Mean_Q61']

# Initialize empty DataFrame to store final results
result = pd.DataFrame()

# Calculate mean, standard deviation, and sample size for each group
result['mean'] = grouped.mean()
result['std_dev'] = grouped.std()
result['sample_size'] = grouped.count()

# Calculate standard error
result['std_err'] = result['std_dev'] / np.sqrt(result['sample_size'])

# Calculate 95% confidence intervals
result['lower_95'] = result['mean'] - 1.96 * result['std_err']
result['upper_95'] = result['mean'] + 1.96 * result['std_err']

# Format to 4 decimal places
result = result.round(4)

# Map Mean_incomeWB numbers to categories
result.index = result.index.map({1: 'Low', 2: 'Lower-middle', 3: 'Upper-middle', 4: 'High'})

# Plotting DataFrame as an image
fig, ax = plt.subplots(figsize=(12, 4))  # set the size that you'd like (width, height)
ax.axis('tight')
ax.axis('off')
plt.title("Trust by Income group")
ax.table(cellText=result.values,
         colLabels=result.columns,
         rowLabels=result.index,
         cellLoc='center', loc='center')

plt.show()



## Moral Relativism
# Group by Mean_incomeWB and calculate relevant statistics
grouped = dataset.groupby('Mean_incomeWB')['Mean_Q176']

# Initialize empty DataFrame to store final results
result = pd.DataFrame()

# Calculate mean, standard deviation, and sample size for each group
result['mean'] = grouped.mean()
result['std_dev'] = grouped.std()
result['sample_size'] = grouped.count()

# Calculate standard error
result['std_err'] = result['std_dev'] / np.sqrt(result['sample_size'])

# Calculate 95% confidence intervals
result['lower_95'] = result['mean'] - 1.96 * result['std_err']
result['upper_95'] = result['mean'] + 1.96 * result['std_err']

# Format to 4 decimal places
result = result.round(4)

# Map Mean_incomeWB numbers to categories
result.index = result.index.map({1: 'Low', 2: 'Lower-middle', 3: 'Upper-middle', 4: 'High'})

# Plotting DataFrame as an image
fig, ax = plt.subplots(figsize=(12, 4))  # set the size that you'd like (width, height)
ax.axis('tight')
ax.axis('off')
plt.title("Moral Relativism by Income group")
ax.table(cellText=result.values,
         colLabels=result.columns,
         rowLabels=result.index,
         cellLoc='center', loc='center')

plt.show()
