#Write a function to calculate the Fibonacci sequence up to a certain limit.

def fibonacci_sequence(limit):
    
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    
    sequence = [0, 1]  
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence if limit > 0 else [0]

try:
    user_limit = int(input("Enter the limit for the Fibonacci sequence: "))
    print(f"Fibonacci sequence up to {user_limit}: {fibonacci_sequence(user_limit)}")
except ValueError:
    print("Please enter a valid non-negative integer.")
