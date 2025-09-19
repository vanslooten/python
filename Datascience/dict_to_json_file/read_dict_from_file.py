import json

f = open("person_data.json")
filecontent = f.read()
# print(filecontent)

# convert JSON string back to Python dict:
data = json.loads(filecontent)

print(type(data))
print(data)
