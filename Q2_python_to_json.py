# Q.2 Python object ko json data main convert karne ka program likho?

# Example:

# Input :-

# Output:-

import json


a={
    "name": "David", 
    "class": "I", 
    "age": 6
    }
b=json.dumps(a)
print(b)
print(type(b))