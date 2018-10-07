# JSON processing
"""
json.load() -  It reads the string from the file, parses the JSON data and populates as a Python Dict
json.dump()  - To write the JSON (in the form of Python Dict) to the outfile file. It transforms your Python dict object into the serialized JSON string.
"""
import json

# Example to write JSON to file
json_data = '{ "name":"Java", "latestVersion":11, "platform":"JEE"}' #  JSON (Python Dict)

with open('json_data.txt', 'w') as outfile:
    json.dump(json_data, outfile)   # # writes Python Dict to file
    print('Written JSON to json_data.txt')
    print()

# ---------------------------------------------------------------------

# Example to read JSON from file
with open('json_data1.txt') as json_file:
  pythonDict = json.load(json_file)   # returns Python Dict

for x, y in pythonDict.items():
  print(x, y)

