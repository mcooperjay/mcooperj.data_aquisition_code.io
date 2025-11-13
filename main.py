import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Proper resource ID for Leading Causes of Death
cdc_url = "https://data.cdc.gov/resource/bi63-dtpu.json?$limit=50000"

r = requests.get(cdc_url)
data = r.json()

print(type(data))
print(len(data)) 

cdc = pd.DataFrame(data)
print(cdc.columns[:10])

cdc.info()
cdc.isna().sum()
cdc['deaths'] = pd.to_numeric(cdc['deaths'], errors='coerce')
cdc['aadr'] = pd.to_numeric(cdc['aadr'], errors='coerce')
cdc['year'] = pd.to_numeric(cdc['year'], errors='coerce')

cdc = cdc.dropna(subset=['year', 'state', 'deaths'])
cdc.head()

cdc = cdc[cdc['cause_name'] != 'All causes']

deaths_per_year = cdc.groupby('year')['deaths'].sum()
ranked_causes = cdc.groupby('cause_name')['deaths'].sum().sort_values(ascending=False)
state_cause = cdc.groupby(['state', 'cause_name'])['deaths'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x=ranked_causes.head(10).values, y=ranked_causes.head(10).index, palette='viridis')
plt.title('Top 10 Causes of Death')
plt.xlabel('Total Deaths')
plt.ylabel('Cause')
plt.show()
#Option 2
deaths_by_year = cdc.groupby('year')['deaths'].sum().reset_index()
deaths_by_year.plot(x='year', y='deaths', kind='line', title='Total Deaths by Year')

#option 3
cdc['aadr'] = pd.to_numeric(cdc['aadr'], errors='coerce')
cdc = cdc.dropna(subset=['aadr'])
cdc = cdc[cdc['aadr'] > 0]
state_aadr = cdc.groupby('state')['aadr'].mean().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x = state_aadr.head(20).values, y=state_aadr.head(20).index, palette="magma")
plt.title('Top 20 states by Average Age Adjusted Death Rate')
plt.xlabel('Average AADR per 100000')
plt.ylabel('State')
plt.show()

cdc.to_csv('cdc_mortality_clean.csv', index=False)
