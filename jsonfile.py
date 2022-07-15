import json

key1=["name","designation","age","salary"]
list1=["neelam","programer",24,2400]
list2=["komal","trainer",24,20000]
list3=["anuradha","HR",25,40000]
list4=["Abhishek","manager",29,63000]
emp1={}
emp2={}
emp3={}
emp4={}
for i in range(len(list1)):
    emp1.update({key1[i]:list1[i]})
    emp2.update({key1[i]:list2[i]})
    emp3.update({key1[i]:list3[i]})
    emp4.update({key1[i]:list4[i]})
print(emp1)
print(emp2)
print(emp3)
print(emp4)

data={1:emp1,2:emp2,3:emp3,4:emp4}
with open("data of student.json","w") as write:
    json.dump(data ,write,indent=5)


# import json























# list=[
#     ["neelam","programer",24,2400],
#     ["komal","trainer",24,20000],
#     ["anuradha","HR",25,40000],
#     ["Abhishek","manager",29,63000]  
# ]
# key1=["name","designation","age","salary"]
# d={}
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         d[key1[i]]=list[j][i]
# print(d)
# with open("student.json","w")as write:
#     json.dump(d,write,indent=5)
