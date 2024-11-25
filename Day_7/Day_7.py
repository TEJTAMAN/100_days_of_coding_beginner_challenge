#Create a program that converts temperatures betweenCelsius, Fahrenheit, and Kelvin


Units = (input("Please enter the scale of your temperature in Celsius, Farenheit, Kelvin: ")).lower()
if Units == "celsius":
    temperature = float(input("Please enter the temprature: "))
    temp_farenheit = (temperature * (9/5)) + 32
    print(f"The givem Temperature in Farenheit is: {temp_farenheit:.2f}")

    temp_kelvin = temperature + 273.15
    print(f"The given Temperature in Kelvin is: {temp_kelvin:.2f}")
    
elif Units == "farenheit":
    
    temperature = float(input("Please enter the temperature: "))
    temp_celsius = (temperature - 32) * 5/9
    print(f"The given temperatue in Celsius is: {temp_celsius:.2f} ")
    
    temp_kelvin = temp_celsius + 273.15
    print(f"The given temperature in Kelvin is: {temp_kelvin:.2f}")

elif Units == "kelvin":

    temperature = float(input("Please enter the temperature: "))
    temp_celsius = temperature - 273.15
    print(f"The given temperature in Celsius is: {temp_celsius:.2f}")

    temp_farenheit = (temp_celsius * (9/5)) + 32
    print(f"The given temperature in Farenheit is: {temp_farenheit:.2f}")

else:
    print("Please enter valid input")

    