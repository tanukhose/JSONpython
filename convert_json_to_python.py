# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
# print(type(y))


# a="Tanuja"
# i=0
# while i<len(a):
#     if i%2==0:
#         print("even")
#         i=i+1

# a="Tanuja"
# c=0
# c1=0
# for i in a:
#     if i=="A" or i=="E" or i=="I" or i=="U" or i=="O" and i=="e" or i=="o" or i=="u" or i=="a" or i=="u":
#         c=c+1
#     else:
#         c1=c1+1
# print("vowel",c)
# print("consanant",c1)

# a=int(input("enter the number"))
# i=a
# s=0
# while i<=a:
#     if a%i==0:
#         s=s+i
#     i=i+1
# if s==a:
#     print("perfect number")
# else:
#     print("not perfect number")

# i=1
# while i<=5:
#     j=0
#     while j<=5-i:
#         print(" ",end=" ")
#         j=j+1
#     b=1
#     while b>=1:
#         print(b,end=" ")
#         b=b+1
#     a=2
#     while a<=i:
#         print(a,end=" ") 
#         a=a+1
#     print()
#     i=i+1

i=1
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print(i,"prime number")
    else:
        print(i,"not prime number")
    i+=1


