#Append data to an existing text file.



# Open the file in append mode
with open("example.txt", "a") as file:
    # Append new data
    file.write("This is the new line of text.\n")
