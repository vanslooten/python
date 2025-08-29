
# https://www.w3schools.com/python/python_user_input.asp

name = input("Enter your name: ")
print("Hello", name)

temperature_input = input("Enter temperature: ")
if temperature_input.isnumeric():
    # Convert the input to a float for calculations 
    temperature = float(temperature_input)
    print("Temperature:", temperature)
else:
    print("Invalid input or temperature.")
