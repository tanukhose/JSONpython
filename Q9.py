# Questions_Question9
# Q.9 Apki pass ek shopping name ki ek dictionary hai

# Code Example
# {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

# Apki dictionary ka use kar ke ek json file create karna hai.
# Aur apko kuch task perform karne hai jaise ki

# 1

# main dekhna chahta hu shopping list ko json file dekhna.

# 2

# phir main user se poochu ga ki kon sa item khareedna chahte ho.

# 3

# uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.

# 4

# phir aapka wo number of items json file se remove karna hai.

# 5

# Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.





# Output:-


# Code Example
# show shopping_list:- 

# {
#     "shopping_list":{ 
#         "chaco":"15",
#         "Biscuits":"50",
#         "Diary_milk":"30",
#         "ice_cream":"20",
#          } 
# }

# Code Example
# {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
import json



li={
    "shopping_list":{ 
        "chaco":"15",
        "Biscuits":"50",
        "Diary_milk":"30",
        "ice_cream":"20",
         } 
    }
ur=input("enter the choice")
del li["shopping_list"][ur]
# print(li)
with open("shopping.json",'w')as wr:
    json.dump(li,wr,indent=5)