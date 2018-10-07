# JSON processing
"""
json.loads() -  Convert from JSON to Python dictionary
json.dumps()   -  Convert Python object (dict) to a JSON string
"""


import json

# Example to Convert from JSON to Python
languageJson = '{ "name":"Java", "latestVersion":11, "platform":"JEE"}' #  JSON
languagePythonDict = json.loads(languageJson)    # Convert from JSON to Python dictionary

# Result is a Python dictionary
print("latestVersion: " , languagePythonDict["latestVersion"])
print()

# --------------------------------------------------------
# Example Convert from Python to JSON
#  Python object (dict)
languagePythonDict = {
  "name": "Java",
  "latestVersion": 11,
  "platform": "JEE"
}

# Convert Python object (dict) to a JSON
jsonStr = json.dumps(languagePythonDict)
print()
# Convert Python object (dict) to a JSON using indent
jsonStr = json.dumps(languagePythonDict, indent=4)

# Result is a JSON string
print(jsonStr)