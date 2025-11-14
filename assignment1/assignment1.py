# Task 1: Hello


def hello():
    return "Hello!"


# Task 2: Greet with a Formatted String


def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator


def calc(operand1, operand2, operator="multiply"):
    try:
        match operator:
            case "add":
                return operand1 + operand2
            case "subtract":
                return operand1 - operand2
            case "multiply":
                return operand1 * operand2
            case "divide":
                return operand1 / operand2
            case "modulo":
                return operand1 % operand2
            case "int_divide":
                return operand1 // operand2
            case "power":
                return operand1**operand2
            case _:
                return f"Invalid operator: {operator}"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operator} those values!"


print()
print("10 + 2 = ", calc(10, 2, "add"))
print("10 - 2 = ", calc(2, 10, "subtract"))
print("10 * 2 = ", calc(10, 2, "multiply"))
print("10 / 2 = ", calc(10, 2, "divide"))
print("10 / 0 = ", calc(10, 0, "divide"))
print("10 % 2 = ", calc(10, 2, "modulo"))
print("10 % 0 = ", calc(10, 0, "modulo"))
print("10 // 2 = ", calc(10, 2, "int_divide"))
print("10 // 0 = ", calc(10, 0, "int_divide"))
print("10 ** 2 = ", calc(10, 2, "power"))
print("10 ** 0 = ", calc(10, 0, "power"))
print("'10' * 2 = ", calc("10", 2, "multiply"))
print("'10' * '2' = ", calc("10", "2", "multiply"))
print("'10' + '2' = ", calc("10", "2", "add"))


# Task 4: Data Type Conversion


def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return f"Invalid data type: {data_type}"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


print()
print("'00012' converted to int = ", data_type_conversion("00012", "int"))
print("'5.5000' converted to float = ", data_type_conversion("5.5", "float"))
print("17 converted to float = ", data_type_conversion(17, "float"))
print("36.6 converted to int = ", data_type_conversion(36.6, "int"))
print("'36.6' converted to int = ", data_type_conversion("36.6", "int"))
print("'36.6' converted to float = ", data_type_conversion("36.6", "float"))


# Task 5: Grading System, Using *args


def grade(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Invalid data was provided."
        if arg < 0 or arg > 100:
            return "Invalid data was provided."
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."


print()
print("Grade for 75, 80, 85 = ", grade(75, 85, 95))
print(
    "Grade for 'seventy five', 'eighty', 'eighty five' = ",
    grade("seventy five", "eighty", "eighty five"),
)
print("Grade for 74.5, 80, 85 = ", grade(74.5, 80, 85))
print("Grade for -34, 90, 100 = ", grade(-34, 90, 100))
print("Grade for 110, 90, 100 = ", grade(101, 90, 100))


# Task 6: Use a For Loop with a Range
def repeat(string, times):
    if not isinstance(times, int):
        return "Invalid data was provided."
    if times < 0:
        return "Invalid data was provided."
    if not isinstance(string, str):
        return "Invalid data was provided."

    result = ""
    for i in range(times):
        result += string
    return result


print("Repeat 'Ha' 3 times = ", repeat("Ha", 3))
print("Repeat 'Ha' 0 times = ", repeat("Ha", 0))
print("Repeat 'Ha' -1 times = ", repeat("Ha", -1))
print("Repeat 'Ha' 1.5 times = ", repeat("Ha", 1.5))
print("Repeat 'Ha' 'three' times = ", repeat("Ha", "three"))
print("Repeat 'Ha' [1, 2, 3] times = ", repeat("Ha", [1, 2, 3]))
