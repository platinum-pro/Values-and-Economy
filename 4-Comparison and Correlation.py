import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns



# Load data
dataset = pd.read_csv('C:/filepath/Mean WVS + Econ by Country.csv')


# Leisure vs Income group
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_incomeWB', y='Mean_Q3', data=dataset, color = 'blue')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Low', 'Lower-middle', 'Upper-middle', 'High'])
plt.title('Scatter Plot between Leisure and income group')
plt.ylabel('Leisure')
plt.xlabel('Income Group')
plt.show()


# Leisure vs GDP
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_GDPpercap1', y='Mean_Q3', data=dataset, color = 'blue')
plt.title('Scatter Plot between Leisure and GDP')
plt.ylabel('Leisure')
plt.xlabel('GDP')
plt.show()


# Trust vs Income group
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_incomeWB', y='Mean_Q61', data=dataset, color = 'green')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Low', 'Lower-middle', 'Upper-middle', 'High'])
plt.title('Scatter Plot between Trust and income group')
plt.ylabel('Trust')
plt.xlabel('Income Group')
plt.show()

# Trust vs GDP
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_GDPpercap1', y='Mean_Q61', data=dataset, color = 'green')
plt.title('Scatter Plot between Trust and GDP')
plt.ylabel('Trust')
plt.xlabel('GDP')
plt.show()


# Relativism vs Income group
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_incomeWB', y='Mean_Q176', data=dataset, color = 'orange')
plt.title('Scatter Plot between Moral Relativism and income group')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Low', 'Lower-middle', 'Upper-middle', 'High'])
plt.ylabel('Trust')
plt.xlabel('Income Group')
plt.show()

# Relativism vs GDP
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_GDPpercap1', y='Mean_Q176', data=dataset, color = 'orange')
plt.title('Scatter Plot between Moral Relativism and GDP')
plt.ylabel('Trust')
plt.xlabel('GDP')
plt.show()



# Leisure vs Relativism
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mean_Q3', y='Mean_Q176', data=dataset, color = 'black')
plt.title('Scatter Plot between Moral Relativism and Leisure')
plt.ylabel('Moral Relativism')
plt.xlabel('Leisure')
plt.show()


# Trust vs Relativism
plt.figure(figsize=(10, 6))
# Get the maximum value for setting y-axis limit
# max_value = dataset['Mean_Q176'].max()
# ax = sns.scatterplot(x='Mean_Q61', y='Mean_Q176', data=dataset, color = 'black')
# ax.set(ylim=(0, max_value))
sns.scatterplot(x='Mean_Q61', y='Mean_Q176', data=dataset, color = 'black')
plt.title('Scatter Plot between Moral Relativism and Trust')
plt.ylabel('Moral Relativism')
plt.xlabel('Trust')
plt.show()
