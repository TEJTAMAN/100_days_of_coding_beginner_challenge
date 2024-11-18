def _type(input_value):

    try:
        int(input_value)
        return "Integer"
    except:
        pass

    try:
        float(input_value)
        return "float"
    except:
        pass

    return "String"

user_input = input("Enter something: ")
input_type = _type(user_input)
print(f"the type of input is: {input_type}")
        