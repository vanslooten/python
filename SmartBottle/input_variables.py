
# https://www.w3schools.com/python/python_user_input.asp

# temperature input and verification
temperature_input = input("Enter temperature: ")
if temperature_input.isnumeric():
    # Convert the input to a float for calculations 
    temperature = float(temperature_input)
    print("Temperature:", temperature)
else:
    print("Invalid input or temperature.")
    temperature = None

# cap status input and verification
isCapOn_input = input("Is the cap on? (yes/no): ")
if isCapOn_input.lower() in ['yes', 'y']:
    isCapOn = True
    print("The cap is on.")
elif isCapOn_input.lower() in ['no', 'n']:
    isCapOn = False
    print("The cap is off.")
else:
    print("Invalid input for cap status.")
    isCapOn = None  

# input a list of alerts
alerts_input = input("Enter a list of alerts separated by commas: ")  
if alerts_input:
    alerts = [s.strip() for s in alerts_input.split(',')]
    print("Alerts:", alerts)
else:
    print("No alerts entered.")
    alerts = []


