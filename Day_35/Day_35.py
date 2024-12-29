#Calculate the average of numbers in a text file.


def calculate_average(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read numbers from the file and clean the data
            numbers = []
            for line in file:
                # Split line by whitespace, commas, etc., and convert to floats
                numbers.extend([float(num) for num in line.split() if num.strip().replace('.', '', 1).isdigit()])
            
        if not numbers:
            return "No numbers found in the file."
        
        average = sum(numbers) / len(numbers)
        return f"The average of the numbers is: {average}"
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."
    except Exception as e:
        return f"An error occurred: {e}"

