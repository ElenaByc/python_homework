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

# 3.4 Display information about the DataFrame
print("Information about the DataFrame")
print(more_employees.info())
print()

# Task 4
print("--------------------------------")
print("Task 4")
print("--------------------------------")
print()

# 4.1 Read dirty data and create a copy
dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()

print("Original dirty data")
print(dirty_data)
print()

print("Copy of dirty data")
print(clean_data)
print()

# 4.2 Remove duplicate rows
clean_data = clean_data.drop_duplicates()

print("Data after removing duplicates")
print(clean_data)
print()

# 4.3 Convert Age to numeric
# clean_data['Age'] = pd.to_numeric(
#     clean_data['Age'],
#     errors='coerce'
# )  -  gives a warning

# clean_data.loc[:, 'Age'] = pd.to_numeric(
#     clean_data['Age'],
#     errors='coerce'
# )  - test failed

clean_data = clean_data.assign(
    Age=pd.to_numeric(clean_data['Age'], errors='coerce')
)

print("Age converted to numeric")
print(clean_data['Age'])
print(clean_data['Age'].dtype)
print()

# # 4.4 Convert Salary to numeric
# clean_data['Salary'] = pd.to_numeric(
#     clean_data['Salary'],
#     errors='coerce'
# ) - gives a warning

clean_data = clean_data.assign(
    Salary=pd.to_numeric(clean_data['Salary'], errors='coerce')
)

print("Salary converted to numeric")
print(clean_data['Salary'])
print(clean_data['Salary'].dtype)
print()

# # 4.5 Fill missing values
# clean_data['Age'] = clean_data['Age'].fillna(
#     clean_data['Age'].mean()
# ) - gives a warning

# clean_data['Salary'] = clean_data['Salary'].fillna(
#     clean_data['Salary'].median()
# ) - gives a warning

clean_data = clean_data.assign(
    Age=clean_data['Age'].fillna(clean_data['Age'].mean()),
    Salary=clean_data['Salary'].fillna(clean_data['Salary'].median())
)

print("Data after filling missing values")
print(clean_data)
print()
