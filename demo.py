# importing libraries
import json

def validate(filename):
    with open(filename) as file:
        try:
            return json.load(file) # put JSON-data to a variable
        except json.decoder.JSONDecodeError:
            print("Invalid JSON") # in case json is invalid
        else:
            print("Valid JSON") # in case json is valid

json_file = validate(r"REPLACE FILE PATH")
print(json_file)
