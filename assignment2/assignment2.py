import csv
import os
import traceback
import custom_module
from pprint import pprint
from datetime import datetime


# Task 2: Read a CSV File
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


# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    result_dict = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        employee_info = employee_dict(row)
        result_dict[employee_id] = employee_info

    return result_dict


all_employees = all_employees_dict()
print("All employees dictionary:")
pprint(all_employees)


# Task 10: Use the os Module
def get_this_value():
    return os.getenv("THISVALUE")


this_value = get_this_value()
print("THISVALUE environment variable:", this_value)


# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


print("custom_module.secret before setting:", custom_module.secret)
set_that_secret("supersupersecret")
print("custom_module.secret after setting:", custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv


# Helper function to read a CSV file into a dictionary
# similar to read_employees() function
def read_csv_file(file_name):
    result_dict = {}
    data_rows = []

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", file_name)
        with open(csv_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if "fields" not in result_dict:
                    result_dict["fields"] = row
                else:
                    data_rows.append(tuple(row))

        result_dict["rows"] = data_rows
        return result_dict

    except Exception as e:
        print(f"Error happened while reading {file_name}")
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


def read_minutes():
    minutes1 = read_csv_file("minutes1.csv")
    minutes2 = read_csv_file("minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print("Minutes1:")
pprint(minutes1)
print("Minutes2:")
pprint(minutes2)
print(
    f"Minutes 1 and munites 2 total length: {len(minutes1['rows'])} + {len(minutes2['rows'])} = {len(minutes1['rows']) + len(minutes2['rows'])}"
)


# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2


minutes_set = create_minutes_set()
print(f"Minutes set (set length is {len(minutes_set)}):")
pprint(minutes_set)


# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    result = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )
    return result


minutes_list = create_minutes_list()
print("Minutes list:")
pprint(minutes_list)


# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda item: item[1])
    formatted_rows = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes)
    )

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "minutes.csv")
        with open(csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(formatted_rows)
    except Exception as e:
        print("An error occurred while writing minutes.csv")
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

    return formatted_rows


formatted_list = write_sorted_list()
print("minutes.csv has been written")
print("Formatted list:")
pprint(formatted_list)
