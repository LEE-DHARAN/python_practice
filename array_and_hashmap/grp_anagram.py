from collections import defaultdict


# fruits = ["mango","banana","pineapple"]
# fruits.append("orange")
# veggies = ["brinjal","potato","drumsticks"]
# groceries = [fruits,veggies]
# for fruit in fruits:
#     print(fruit)
# for gro in groceries:
#     for g in gro:
#         print(g)    

fruits = ["mango","banana","pineapple"]
hash_map = defaultdict(list) #emptylist
hash_map["fruits"].append("mango")
hash_map["fruits"].append("orange")       
print(hash_map["fruits"])