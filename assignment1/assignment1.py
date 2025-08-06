# Write your code here.

# Task 1

def hello ():
    return "Hello!"

# Task 2 

def greet (name):
    return (f"Hello, {name}!")

# Task 3

def calc (a, b, operation = "multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Unknown Operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4

def data_type_conversion(value, type):
    try: 
        if type == "float":
            return float(value)
        elif type == "int":
            return int(value)
        elif type == "str":
            return str(value)
        else:
            return f"{type} is Unsupported!"
    except (ValueError, TypeError):
        return (f"You can't convert {value} into a {type}.")

# Task 5

def grade(*args):
    try: 
        average = sum(args) / len(args)
   
        if average >= 90:
            return "A"
        elif 80 <= average < 90:
            return "B"
        elif 70 <= average < 80:
            return "C"
        elif 60 <= average < 70:
            return "D"
        else: 
            return "F"
    except(TypeError, ZeroDivisionError):
        return "Invalid data was provided."
# Task 6

def repeat (string, count):
    result = ""
    for i in range(count):
        result += string
    return result
# Task 7

def student_scores(mode, **kwargs):
    if mode == "best":
        best_student = max(kwargs, key = kwargs.get)
        return best_student
    elif mode == "mean":
        if kwargs:
            average = sum(kwargs.values()) / len(kwargs)
            return average
        else:
            return 0
    else: 
        return "Invalid mode"

# Task 8

def titleize(title_string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title_string.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())  # Always capitalize first and last
        elif word.lower() in little_words:
            result.append(word.lower())       # Keep little words lowercase
        else:
            result.append(word.capitalize())  # Capitalize other words

    return " ".join(result)
    
# Task 9

def hangman(secret, guess):
    result = ""

    for letter in secret: 
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# Task 10

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            pig_word = word[2:] + "quay"
        elif word[0] in vowels:
            pig_word = word + "ay"
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            pig_word = word[i:] + word[:i] + "ay"

        result.append(pig_word)

    return " ".join(result)