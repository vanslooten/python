# https://www.w3schools.com/python/python_json.asp

import json

# a Python object (dict):
person_data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
json_string = json.dumps(person_data)

# the result is a JSON string:
print(json_string)

# create file:
f = open("person_data.json", "x")
         
# write JSON string to file:
f.write(json_string)
f.close()
