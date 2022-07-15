# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# Example
# Input :-
# Code Example

# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

# Output:-
# Code Example
# Json_file.json:-


# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }

import json

a={"Name": "Abhishek","Designation":"CEO of navgurukul","Gender": "male","Age": '29'}
with open("Q7data.json","w")as wr:
    json.dump(a,wr,indent=4)

with open("Q7data.json",'r')as re:
    print(json.load(re))

    