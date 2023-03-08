
#Import all necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#Checking if file exists while cleaning data
if os.path.isfile("C:\\Users\\GLFos\\Documents\\Data Visualization CSV\\all_data.csv"):
    #Extract data from the CSV file
    data = pd.read_csv("C:\\Users\\GLFos\\Documents\\Data Visualization CSV\\all_data.csv")
    print(data.head())

    #Check for missing values
    print(data.isnull().sum())

    #Drop rows with missing values
    data = data.dropna()

    #Print unique values
    print(data.Country.unique())
    print(data.Year.unique())
else:
    print("File not found!")

#Calculate correlation coefficient (Weak / Medium)
corr_coef = data['GDP'].corr(data['Life expectancy at birth (years)'])
print('Correlation coefficent', corr_coef)

#Visualize Data
#Life expectancy by GDP
sns.scatterplot(x='Life expectancy at birth (years)', y='GDP', hue='Country', data=data)
plt.show()

#Life expectancy by country
plt.figure(figsize=(8,6))
sns.barplot(x="Life expectancy at birth (years)", y="Country", data=data)
plt.xlabel("Life expectancy at birth (years)")
plt.show()

#Life expectancy by year
plt.figure(figsize=(8,6))
sns.lineplot(x='Year', y='Life expectancy at birth (years)', hue='Country', data=data)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("Life expectancy at birth (years)")
plt.show()

#GDP by country
plt.figure(figsize=(8,6))
sns.barplot(x="GDP", y="Country", data=data)
plt.xlabel("GDP in Trillions of U.S. Dollars")
plt.show()

#GDP by year
plt.figure(figsize=(8,6))
sns.lineplot(x='Year', y='GDP', hue='Country', data=data)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.show()

