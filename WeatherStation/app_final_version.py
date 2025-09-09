# Accompanying tutorial:
# https://home.et.utwente.nl/slootenvanf/2024/05/02/python-weather-station-app/
#
# some info that was helpful developing this script:
# https://stackoverflow.com/questions/30489308/creating-a-custom-widget-in-tkinter
#
# Output Formatting
# https://docs.python.org/3/tutorial/inputoutput.html

import tkinter as tk
from WeatherStation import WeatherStation

class TemperaturePanel(tk.Frame):
    w = "" # WeatherStation
    temperature = "20.0"
    humidity = "50"
    
    def __init__(self, parent, id):
        tk.Frame.__init__(self, parent)
        self.configure(background="#ffffff", borderwidth=5)
        
        self.w = WeatherStation(id)
        self.temperature = self.w.readTemperature()
        self.humidity = self.w.readValue('luchtvochtigheid')

        self.labelTemp = tk.Label(self, text=self.temperature, anchor="center", font=("Arial", 25))
        self.labelHumidity = tk.Label(self, text="Humidity: "+self.humidity+"%", anchor="center")
        self.lblStationName = tk.Label(self, text=self.w.readNameStation(), anchor="center")

        self.labelTemp.pack(side="top", fill="both")
        self.labelHumidity.pack(side="top", fill="both")
        self.lblStationName.pack(side="top", fill="both")

    def readTemperature(self):
        # read temperature from the WeatherStation:
        temperature_str = self.w.readValue('temperatuurGC');
        # converts temperature to a float:
        temperature_value = float(temperature_str)
        return temperature_value

class Frame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.panel1 = TemperaturePanel(self, 6290)
        self.panel2 = TemperaturePanel(self, 6310)
        self.panel3 = TemperaturePanel(self, 6240)
        self.panel4 = TemperaturePanel(self, 6242)
        
        self.panel1.grid(row=0, column=0, sticky="ew")
        self.panel2.grid(row=0, column=1, sticky="ew")
        self.panel3.grid(row=1, column=0, sticky="ew")
        self.panel4.grid(row=1, column=1, sticky="ew")

        # 2 equal sized columns:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # calculate avarage and display that:
        average = (self.panel1.readTemperature()+self.panel2.readTemperature()+self.panel3.readTemperature()+self.panel4.readTemperature())/4;
        print("average:", average)
        #avarage_txt=f'Average temperature: {average:.1f}'
        self.label = tk.Label(self, text=f'Average temperature: {average:.1f}', anchor="center")
        self.label.grid(row=2, column=0, columnspan=2, sticky="ew")

# main script:

root = tk.Tk()
root.geometry("500x250")
root.title("WeatherStation")
Frame(root).place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()
