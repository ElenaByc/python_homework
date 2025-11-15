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


print()
print("Repeat 'Ha' 3 times = ", repeat("Ha", 3))
print("Repeat 'Ha' 0 times = ", repeat("Ha", 0))
print("Repeat 'Ha' -1 times = ", repeat("Ha", -1))
print("Repeat 'Ha' 1.5 times = ", repeat("Ha", 1.5))
print("Repeat 'Ha' 'three' times = ", repeat("Ha", "three"))
print("Repeat 'Ha' [1, 2, 3] times = ", repeat("Ha", [1, 2, 3]))


# Task 7: Student Scores, Using **kwargs
def student_scores(operation, **kwargs):
    match operation:
        case "mean":
            try:
                return sum(kwargs.values()) / len(kwargs)
            except (TypeError, ZeroDivisionError):
                return "Invalid data was provided."
        case "best":
            best_student = None
            best_score = -1
            for name, score in kwargs.items():
                if not isinstance(score, (int, float)):
                    return "Invalid data was provided."
                if score < 0 or score > 100:
                    return "Invalid data was provided."
                if score > best_score:
                    best_score = score
                    best_student = name
            return best_student
        case _:
            return f"Invalid operation: {operation}"


print()
student_score_dictionary = {"Anna": 89, "Andrew": 78, "Angela": 67}
print(student_score_dictionary)
print("Mean score = ", student_scores("mean", **student_score_dictionary))
print("Best score = ", student_scores("best", **student_score_dictionary))
print("Invalid operation = ", student_scores("invalid", **student_score_dictionary))

student_score_dictionary = {"Anna": 0, "Andrew": 0, "Angela": 0}
print(student_score_dictionary)
print("Mean score = ", student_scores("mean", **student_score_dictionary))
print("Best score = ", student_scores("best", **student_score_dictionary))


# Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []

    for i, word in enumerate(words):
        # First word is always capitalized
        if i == 0:
            result.append(word.capitalize())
        # Last word is always capitalized
        elif i == len(words) - 1:
            result.append(word.capitalize())
        # Middle words: capitalize unless it's a little word
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)


print()
print("Titleize 'learNing python Is fun' = ", titleize("learNing python Is fun"))
print("Titleize '' = ", titleize(""))
print("Titleize 'one' = ", titleize("one"))
print("Titleize 'one two' = ", titleize("one two"))
print("Titleize 'one two three' = ", titleize("one two three"))
little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
little_words_string = " ".join(little_words)
print(f"Titleize {little_words_string} = ", titleize(little_words_string))


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result


print()
print("Hangman 'apple' 'al' = ", hangman("apple", "al"))
print("Hangman 'banana' 'a' = ", hangman("banana", "a"))
print("Hangman 'pomegranate' 'apple' = ", hangman("pomegranate", "apple"))
print("Hangman 'apricot' 'defgh' = ", hangman("apricot", "defgh"))
print(
    "Hangman 'apricot' 'abcdefghijklmnopqrstuvwxyz' = ",
    hangman("apricot", "abcdefghijklmnopqrstuvwxyz"),
)
