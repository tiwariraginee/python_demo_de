import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'John', 'Anna'],
    'Age': [28, 35, 21, 42, 30],
    'City': ['New York', 'Paris', 'London', 'New York', 'Paris'],
    'Salary': [50000, 60000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

# Grouping by 'Name'
grouped = df.groupby('Name')

# Applying aggregation functions
# For example, getting the average salary for each person
average_salary = grouped['Salary'].max()
print(average_salary)
# Applying multiple aggregation functions
summary_stats = grouped['Salary'].agg(['mean', 'sum', 'count'])
print(summary_stats)