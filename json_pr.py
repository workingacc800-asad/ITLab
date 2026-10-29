#1. What is JSON?
# JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format. 
# It is the universal language used by APIs to send and receive data across the web.

# A. Parsing JSON into a Python Dictionary (json.loads)
import json 

# json data recieved as a text string from an API
json_string = '{"agent_name": "SearchBot", "status" : "active", "tasks" : 3}'

# Convert json string into Python Dictionary
data_dict = json.loads(json_string)

print(data_dict["agent_name"])
print(type(json_string))
print(type(data_dict))

# B. Converting Python Data into a JSON String (json.dumps)
payload_dict = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello agent!"}],
    "temperature": 0.7
}

json_str = json.dumps(payload_dict, indent= 4)
print(json_str)