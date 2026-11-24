import pandas as pd

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