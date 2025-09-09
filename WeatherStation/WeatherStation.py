# WeatherStation class that reads & parses info on a remote xml source containing weather data.
# Accompanying tutorial:
# https://home.et.utwente.nl/slootenvanf/2024/05/02/python-weather-station-app/
#
# it uses the ElementTree XML API to parse the XML data:
# https://docs.python.org/3/library/xml.etree.elementtree.html
#
# some info that was helpful developing this script:
# https://stackoverflow.com/questions/59035954/best-way-to-read-parse-xml-url-in-python3
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/21827961/how-to-parse-remote-document

import urllib.request
import xml.etree.ElementTree as ET

class WeatherStation:
    xml = "https://xml.buienradar.nl/"
    id = 6260
    station = None
    
    def __init__(self, id):
        self.id = id
        self.readData()

    def readData(self):
        # open the URL self.xml and store in ElementTree structure:
        with urllib.request.urlopen(self.xml) as response:
            root = ET.fromstring(response.read().decode())

        # find the station with the given id:
        for weerstation in root.iter('weerstation'):
            if self.id == int(weerstation.get('id')):
                self.station = weerstation
                name = weerstation.find('stationnaam') 
                print("readData()", self.id, name.text)

    def readValue(self, value):
        return self.station.find(value).text
    
    def readTemperature(self):
        return self.readValue('temperatuurGC')
    
    def readNameStation(self):
        name = self.readValue('stationnaam')
        return name.replace("Meetstation", "Station")

# Allow code below to execute when the file runs as a script, but not when it’s imported as a module:
if __name__ == "__main__":
    ws = WeatherStation(6290)
    print("temp:", ws.readTemperature())
