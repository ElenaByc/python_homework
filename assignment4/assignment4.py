import pandas as pd
import json

# Task 1
print("--------------------------------")
print("Task 1")
print("--------------------------------")
print()

# 1.1 Create a DataFrame from a dictionary
employees = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(employees)

print("DataFrame created from dictionary")
print(task1_data_frame)
print()

# 1.2 Add a column called Salary to the DataFrame
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print("DataFrame with Salary column added")
print(task1_with_salary)
print()

# 1.3 Create a copy and increment Age by 1
task1_older = task1_with_salary.copy()
#task1_older['Age'] = task1_older['Age'] + 1      -  gives a warning
task1_older.loc[:, 'Age'] = task1_older['Age'] + 1

print("DataFrame with Age increased by 1")
print(task1_older)
print()

# 1.4 Save the DataFrame to a CSV file
task1_older.to_csv('employees.csv', index=False)

print("DataFrame saved to employees.csv")
print()

# Task 2
print("--------------------------------")
print("Task 2")
print("--------------------------------")
print()

# 2.1 Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')

print("DataFrame read from employees.csv")
print(task2_employees)
print()

# 2.2 Read data from a JSON file
additional_employees = [
    {'Name': 'Eve', 'Age': 28, 'City': 'Miami', 'Salary': 60000},
    {'Name': 'Frank', 'Age': 40, 'City': 'Seattle', 'Salary': 95000}
]

with open('additional_employees.json', 'w') as file:
    json.dump(additional_employees, file, indent=4)

print("JSON file created with additional employees")
print()

json_employees = pd.read_json('additional_employees.json')

print("DataFrame read from additional_employees.json")
print(json_employees)
print()

# 2.3 Combine DataFrames
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print("Combined DataFrame")
print(more_employees)
print()

# Task 3
print("--------------------------------")
print("Task 3")
print("--------------------------------")
print()

# 3.1 Get the first three rows
first_three = more_employees.head(3)

print("First three employees")
print(first_three)
print()

# 3.2 Get the last two rows
last_two = more_employees.tail(2)

print("Last two employees")
print(last_two)
print()

# 3.3 Get the shape of the DataFrame
employee_shape = more_employees.shape

print("Shape of the DataFrame")
print(employee_shape)
print()

