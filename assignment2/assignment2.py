# Task 2: Read a CSV File
import csv
import os
import traceback


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
print(employees)


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")
