import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# Set the path to the directory containing the census files
path = r'C:/Users/Laiba/Desktop/bytewise/projectone/US_Census Data Cleaning/'

# Use glob to get a list of all csv files in the directory
all_files = glob.glob(path + "*.csv")
us_census = pd.concat((pd.read_csv(f) for f in all_files))

# Step 2: Inspect the data
print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)

# Step 3: Split the GenderPop column into Men and Women columns and convert them to numerical datatypes
us_census[['Men', 'Women']] = us_census['GenderPop'].str.split("_", expand=True)
us_census['Men'] = pd.to_numeric(us_census['Men'].str[:-1])
us_census['Women'] = pd.to_numeric(us_census['Women'].str[:-1])

# Step 4: Fill in the missing values in Women column
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])

# Step 5: Remove duplicates
us_census = us_census.drop_duplicates()

# Step 6: Make a scatterplot of average income vs proportion of women
plt.scatter(us_census['Women'] / us_census['TotalPop'], us_census['Income'])
plt.xlabel('Proportion of Women')
plt.ylabel('Average Income')
plt.show()

# Step 7: Make histograms for the race categories
us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']] = us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].replace('%', '', regex=True).astype(float)
us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']] = us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].fillna(0)

plt.hist(us_census['Hispanic'])
plt.title('Hispanic')
plt.show()

plt.hist(us_census['White'])
plt.title('White')
plt.show()

plt.hist(us_census['Black'])
plt.title('Black')
plt.show()

plt.hist(us_census['Native'])
plt.title('Native')
plt.show()

plt.hist(us_census['Asian'])
plt.title('Asian')
plt.show()

plt.hist(us_census['Pacific'])
plt.title('Pacific')
plt.show()
