#Handle exceptions for division by zero.


def safe_divide():
    try:
        # Get input from the user
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        
        # Perform division
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Please enter valid numbers."
    else:
        return f"The result is: {result}"

# Call the function
print(safe_divide())
