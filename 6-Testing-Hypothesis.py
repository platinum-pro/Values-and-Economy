import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy import stats
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
import numpy as np

# Load data
dataset = pd.read_csv('C:/filepath.csv')

# Perform ANOVA
model = ols('Mean_Q176 ~ C(Mean_incomeWB)', data=dataset).fit()
aov_table = sm.stats.anova_lm(model, typ=2)

# Calculate partial eta squared
partial_eta_squared = round(aov_table['sum_sq'][0] / (aov_table['sum_sq'][0] + aov_table['sum_sq'][1]), 4)

# One-way ANOVA for p-value
f_stat, p_value = stats.f_oneway(dataset[dataset['Mean_incomeWB'] == 1]['Mean_Q176'],
                                 dataset[dataset['Mean_incomeWB'] == 2]['Mean_Q176'],
                                 dataset[dataset['Mean_incomeWB'] == 3]['Mean_Q176'],
                                 dataset[dataset['Mean_incomeWB'] == 4]['Mean_Q176'])
p_value = round(p_value, 4)

# Group statistics
group_stats = dataset.groupby('Mean_incomeWB')['Mean_Q176'].describe().round(4)
cell_text = []
for row in range(len(group_stats)):
    cell_text.append(group_stats.iloc[row].tolist() + [None, None])

# Add ANOVA results (Partial Eta Squared and p-value) to the table
anova_row = [None]*len(group_stats.columns.tolist()) + [partial_eta_squared, p_value]
cell_text.append(anova_row)

# Create the ANOVA table
fig, ax = plt.subplots(figsize=(12, 8))
the_table = ax.table(cellText=cell_text, 
                     colLabels=group_stats.columns.tolist() + ['Partial Eta^2', 'p-value'],
                     rowLabels=list(group_stats.index) + ['ANOVA'],
                     cellLoc='center', loc='center')

the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
ax.axis('off')
plt.title('ANOVA Table')
plt.show()


# Perform Tukey's HSD
tukey = pairwise_tukeyhsd(endog=dataset['Mean_Q176'], groups=dataset['Mean_incomeWB'], alpha=0.05)

# Convert Tukey's output to a DataFrame for easier manipulation
tukey_df = pd.DataFrame(data=tukey._results_table.data[1:], columns=tukey._results_table.data[0])

# Round the numerical values to 4 decimal places
tukey_df = tukey_df.round(4)

# Display Tukey's result as a table in a matplotlib plot
fig, ax = plt.subplots(1, 1)

ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=tukey_df.values, colLabels=tukey_df.columns, cellLoc = 'center', loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(1.0, 1.0)

plt.title("Tukey's HSD Test")

plt.show()
