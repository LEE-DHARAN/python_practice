from collections import defaultdict
from typing import List


# fruits = ["mango","banana","pineapple"]
# fruits.append("orange")
# veggies = ["brinjal","potato","drumsticks"]
# groceries = [fruits,veggies]
# for fruit in fruits:
#     print(fruit)
# for gro in groceries:
#     for g in gro:
#         print(g)    

# fruits = ["mango","banana","pineapple"]
# hash_map = defaultdict(list) #emptylist
# hash_map["fruits"].append("mango")
# hash_map["fruits"].append("orange")       
# print(hash_map["fruits"])


def grp_anagram(self,wrds:List[str])->List[List[str]]:
    hash_map = defaultdict(list)
    for wrd in wrds:
        count = [0] * 26
        for char in wrd:
            count[ord(char)-ord('a')] += 1
        hash_map[tuple(count)].append(wrd)
    return list(hash_map.values())
