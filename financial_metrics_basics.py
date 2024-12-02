import pandas as pd

# Dummy data
data = {'Revenue': [100000, 200000], 'Cost': [60000, 140000], 'Shares': [1000, 2000], 'EPS': [10, 12]}
df = pd.DataFrame(data)

# Calculate ROI
df['ROI'] = (df['Revenue'] - df['Cost']) / df['Cost'] * 100
print("ROI:\n", df['ROI'])

# Calculate PE Ratio
df['PE_Ratio'] = df['Revenue'] / df['EPS']
print("PE Ratio:\n", df['PE_Ratio'])
