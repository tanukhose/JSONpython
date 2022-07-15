# Q8.Tumhare pass four employes ki details hai list mai:-


# Code Example
# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]

# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-


# Code Example
# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }
import json

key=["name","designation","age","salary"]
list1=["neelam","programer",24,2400]
list2=["komal","trainer",24,20000]
list3=["anuradha","HR",25,40000]
list4=["Abhishek","manager",29,63000]
emp1={}
emp2={}
emp3={}
emp4={}
for i in range(len(list1)):
    emp1[key[i]]=list1[i]
    emp2[key[i]]=list2[i]
    emp3[key[i]]=list3[i]
    emp4[key[i]]=list4[i]
# print(emp1)
# print(emp2)
# print(emp3)
# print(emp4)
d={1:emp1,2:emp2,3:emp3,4:emp4}
with open("Q8 data of students.json",'w')as wri:
    json.dump(d,wri,indent=6)
    