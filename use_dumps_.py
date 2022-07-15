#python to json

# import json
# a={1:'tfd',2:'gfd',3:'gdfd'}
# b=json.dumps(a)
# print(b)

# l=['tanu',"khose",'nav']
# n=json.dumps(l)
# print(n)


#json to python


# a='["2","4"]'
# k=json.loads(a)
# print(k)
# print(type(k))

# a='"tanu"'
# b=(json.loads(a))
# print(type(b))

# a=12.500
# b=json.dumps(a)
# print(type(b))
# print(b)

# f=11.90
# j=json.loads(f)
# print(j)
# print(type(j))

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
