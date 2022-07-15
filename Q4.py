# Questions_Question4
# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

# Example:

# Input :-


# Code Example
# {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}

# Output:-
# JSON data:


# Code Example
# {
#     "1": 3,
#     "2": 4,
#     "4": 5,
#     "6": 7
# }

import json
d={}
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
# a=sorted(a)
# print(a)


b=json.dumps(a,indent=4)
print(b)
print(type(b)