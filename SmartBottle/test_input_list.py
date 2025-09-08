# input a list of alerts seperated by commas
alerts_input = input("Enter a list of alerts separated by commas: ")
if alerts_input:
    alerts = [s.strip() for s in alerts_input.split(',')]
    print("Alerts:", alerts)
else:
    print("No alerts entered.")
    alerts = [] 
