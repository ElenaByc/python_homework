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
