# Q6.Python object key unique key value ko access karne ka program likho?

# Example:

# Input :-


# Code Example
# '{
#  "a":  1,
#  "a":  2,
#  "a":  3, 
#  "a": 4,   
#  "b": 1, 
#  "b": 2
#  }'

# Output:-


# Code Example
# Original Python object:- 

# {
#     "a":  1, 
#     "a":  2, 
#     "a":  3, 
#     "a": 4, 
#     "b": 1, 
#     "b": 2
# }


# Unique Key in a JSON object:-

# {'a': 4, 'b': 2}


import json

n='{ "a":1,"a":  2,"a":  3, "a": 4,"b": 1,"b": 2}'

m=json.loads(n)
print(m)
print(type(m))

