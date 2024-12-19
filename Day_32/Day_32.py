#Read and display the contents of a text file.

# Open the file in read mode
with open('file.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Display the content
    print(content)


#Replace 'file.txt' with the path to your file.