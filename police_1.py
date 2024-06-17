import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\1. APPS\Works\Playground\Project\DATASETS\Police_dataset.csv')
# Define font dictionaries for titles and labels
font1= {'family':'serif','color':'blue','size':10}
font2= {'family':'serif','color':'darkred','size':10}

#Total sum of null values present in which column?
print(data.isnull().sum())

## 1. Remove the column that only contains null / missing values:
data.drop(columns='country_name', inplace=True)
print('>> After removing null values: \n \n', data.isnull().sum())


## 2. For Speeding, if Men or Women are stopped more often?
speeding_data = data[data.violation == 'Speeding']  # Filtering data for speeding violations

gender_counts = speeding_data.driver_gender.value_counts()  # Counting gender distribution
## Plotting the bar chart for gender distribution in speeding violations
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Gender Distribution for Speeding Violations', fontdict=font1)
plt.xlabel('Gender', fontdict=font2)
plt.ylabel('Count',fontdict=font2)
plt.xticks(rotation=0)
plt.show()


## 3.  Does gender affect who gets searched during a stop?
gender_count = data.groupby('driver_gender').search_conducted.sum()
# Plotting the pie chart for searches conducted by gender
gender_count.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['red', 'yellow'])
plt.title('Search Conducted by Gender')
plt.ylabel('')
plt.show()


## 4.  What is the mean stop duration? and Mapping stop duration to numerical values
# we need to convert it into integer:
data['stop_duration'] = data['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 24, '30+ Min': 45})

# Plotting the histogram for stop duration distribution
data['stop_duration'].plot(kind='hist', bins=[0, 15, 30, 45], edgecolor='black')
plt.title('Distribution of Stop Duration',fontdict=font1)
plt.xlabel('Stop Duration (minutes)',fontdict=font2)
plt.ylabel('Frequency',fontdict=font2)
plt.show()

# Now we can calculate the mean value of stop duration column:
mean_stop_duration = data['stop_duration'].mean()
print(f'The mean value of stop_duration column is: {mean_stop_duration:.2f}')



## 5.  Compare the Age distribution for each violation:
# Histogram for Age Distribution by Violation:
violations = data['violation'].unique()
plt.figure(figsize=(12, 8))

for violation in violations:
    subset = data[data['violation'] == violation]
    plt.hist(subset['driver_age'], bins=20, alpha=0.5, label=violation)

plt.title('Age Distribution for Each Violation Type')
plt.xlabel('Driver Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()



## 6. Monthly Trends in Violations: Analyze how violations vary by month to identify any seasonal trends or patterns
# Convert stop_date to datetime and extract month
data['stop_date'] = pd.to_datetime(data['stop_date'])
data['month'] = data['stop_date'].dt.month

# Group by month and violation type
monthly_violations = data.groupby(['month', 'violation']).size().unstack()

# Plotting monthly trends
monthly_violations.plot(kind='line', figsize=(12, 8))
plt.title('Monthly Trends in Violations')
plt.xlabel('Month')
plt.ylabel('Number of Violations')
plt.legend(title='Violation Type')
plt.show()



## 7. Violation Type by Race:
# Group by race and violation type
race_violations = data.groupby(['driver_race', 'violation']).size().unstack()

# Plotting violation type by race
race_violations.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Violation Type by Race')
plt.xlabel('Driver Race')
plt.ylabel('Number of Violations')
plt.legend(title='Violation Type')
plt.xticks(rotation=45)
plt.show()



## 8. Search Conducted vs. Violation Type:
# Analyze if certain types of violations are more likely to result in a search.
search_by_violation = data.groupby(['violation', 'search_conducted']).size().unstack()  # Group by violation type and search conducted

# Plotting search conducted by violation type
search_by_violation.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Search Conducted by Violation Type')
plt.xlabel('Violation Type')
plt.ylabel('Number of Searches')
plt.legend(title='Search Conducted', labels=['No', 'Yes'])
plt.xticks(rotation=45)
plt.show()
