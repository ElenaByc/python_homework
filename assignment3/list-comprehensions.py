import csv

# Read the CSV file into a list of lists
with open('../csv/employees.csv', 'r') as file:
    csv_reader = csv.reader(file)
    employees = list(csv_reader)[1:]

# Create a list of employee names (first_name + space + last_name)
# Skip the header row (index 0)
names = [row[1] + " " + row[2] for row in employees]
print("All names:")
print(names)
print()

# Create a list of names that contain the letter "e"
names_with_e = [name for name in names if "e" in name]
print("Names with 'e':")
print(names_with_e)
