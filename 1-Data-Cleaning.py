import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read the dataset
data = pd.read_csv('C:/filepath/WVS_Cross-National_Wave_7_csv_v5_0.csv')
print(data.head())

unusable_values = {
    'Q1'  : [-1, -2, -4, -5],    'Q2'  : [-1, -2, -4, -5],    'Q3'  : [-1, -2, -4, -5],
    'Q4'  : [-1, -2, -4, -5],    'Q5'  : [-1, -2, -4, -5],    'Q6'  : [-1, -2, -4, -5],
    'Q29' : [-1, -2, -4, -5],    'Q31' : [-1, -2, -4, -5],    'Q33' : [-1, -2, -4, -5],
    'Q34' : [-1, -2, -4, -5],    'Q37' : [-1, -2, -4, -5],    'Q39' : [-1, -2, -4, -5],
    'Q40' : [-1, -2, -4, -5],    'Q41' : [-1, -2, -4, -5],    'Q46' : [-1, -2, -4, -5],
    'Q47' : [-1, -2, -4, -5],    'Q48' : [-1, -2, -4, -5],    'Q49' : [-1, -2, -4, -5],
    'Q50' : [-1, -2, -4, -5],    'Q58' : [-1, -2, -4, -5],    'Q59' : [-1, -2, -4, -5],
    'Q60' : [-1, -2, -4, -5],    'Q61' : [-1, -2, -4, -5],    'Q62' : [-1, -2, -4, -5], 'Q63' : [-1, -2, -4, -5],
    'Q66' : [-1, -2, -4, -5],    'Q69' : [-1, -2, -4, -5],    'Q71' : [-1, -2, -4, -5],
    'Q108': [-1, -2, -4, -5],    'Q109': [-1, -2, -4, -5],    'Q110': [-1, -2, -4, -5],
    'Q112': [-1, -2, -4, -5],    'Q121': [-1, -2, -4, -5],    'Q130': [-1, -2, -4, -5],
    'Q131': [-1, -2, -4, -5],    'Q158': [-1, -2, -4, -5],    'Q159': [-1, -2, -4, -5],
    'Q161': [-1, -2, -4, -5],    'Q164': [-1, -2, -4, -5],    'Q169': [-1, -2, -4, -5],
    'Q170': [-1, -2, -4, -5],    'Q171': [-1, -2, -4, -5],    'Q172': [-1, -2, -4, -5],
    'Q176': [-1, -2, -4, -5],    'Q235': [-1, -2, -4, -5],    'Q236': [-1, -2, -4, -5],
    'Q239': [-1, -2, -4, -5],    'Q240': [-1, -2, -4, -5],    'Q252': [-1, -2, -4, -5],
    'Q253': [-1, -2, -4, -5],    'Q254': [-1, -2, -4, -5],}

# Dictionary of variables to reverse-code and their respective maximum values
reverse_vars = {
    'Q29': 4, 'Q31': 4, 'Q33': 5, 'Q34': 5, 'Q37': 5, 'Q39': 5, 'Q40': 5, 
    'Q41': 5, 'Q46': 4, 'Q47': 5, 'Q58': 4, 'Q59': 4, 'Q60': 4, 'Q61': 4, 
    'Q62': 4, 'Q63': 4, 'Q66': 4, 'Q69': 4, 'Q71': 4, 'Q131': 4, 'Q169': 4, 
    'Q170': 4, 'Q171': 7, 'Q172': 8, 'Q176': 10, 'Q235': 4, 'Q236': 4, 'Q239': 4, 
    'Q253': 4, 'Q254': 5
}

# Filter out unusable values
for var, values in unusable_values.items():
    data = data[~data[var].isin(values)]

# Reverse-code specified variables directly without creating new columns
for var, max_val in reverse_vars.items():
    data[var] = max_val + 1 - data[var]

# Create a DataFrame to store the means for each variable
means_df = pd.DataFrame()
means_df['B_COUNTRY_ALPHA'] = data['B_COUNTRY_ALPHA'].unique()

# Combine variable lists
all_vars_list = list(set(reverse_vars.keys()) | set(unusable_values.keys()) | set(["regionWB", "incomeWB", "GDPpercap1"]))

# Compute the mean for each variable
for var in all_vars_list:
    mean_values = data.groupby('B_COUNTRY_ALPHA')[var].mean().reset_index()
    mean_values.rename(columns={var: f"Mean_{var}"}, inplace=True)
    means_df = pd.merge(means_df, mean_values, on='B_COUNTRY_ALPHA', how='left')


means_df.to_csv('C:/filepath/Mean WVS + Econ by Country.csv', index=False)

print(means_df)
