# https://www.w3schools.com/python/python_json.asp

import json

dictl = [
{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},
{
  "brand": "Kia",
  "model": "Cando",
  "year": 1969
}
]
print(dictl)

# convert into JSON:
json_string = json.dumps(dictl)

# the result is a JSON string:
print(json_string)

# create file:
f = open("car_data.json", "x")

# write JSON string to file:
f.write(json_string)
f.close()
