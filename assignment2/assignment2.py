# Task 2: Read a CSV File
import csv
import os
import traceback
from pprint import pprint


def read_employees():
    # dictionary to store the CSV structure
    result_dict = {}
    # list to store all data rows
    data_rows = []

    try:
        csv_file_path = os.path.join(
            os.path.dirname(__file__), "..", "csv", "employees.csv"
        )
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if dictionary already has "fields" key
                if "fields" not in result_dict:
                    # Store the first row as column headers under key "fields"
                    result_dict["fields"] = row
                else:
                    # All subsequent rows are data rows - add them to the list
                    data_rows.append(row)

        result_dict["rows"] = data_rows
        return result_dict

    except Exception as e:
        # If any error occurs (file not found, parsing error, etc.)
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)


employees = read_employees()
print("Employees:")
pprint(employees)


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_index]


# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]


sort_by_last_name()
print("Employees sorted by last name:")
pprint(employees)


# Task 8: Create a dict for an Employee

# without using zip()


# Task 8: Create a dict for an Employee

# with using zip()
# def employee_dict(row):
#     result_dict = {}
#
#     for i in range(len(employees["fields"])):
#         field = employees["fields"][i]
#         value = row[i]
#         if field != "employee_id":
#             result_dict[field] = value
#
#     return result_dict


# using zip() - pairs up each field name with its corresponding value in the row
def employee_dict(row):
    result_dict = {}

    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            result_dict[field] = value

    return result_dict
