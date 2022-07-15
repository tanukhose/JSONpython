# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?


import json
a=12+34j
b=json.dumps(a)
print(b)
print(type(b))

# typeError Object of type complex is not JSON serializable