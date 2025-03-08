# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False  

#     char_count = {}

   
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#         print(char_count[char])

  
#     for char in t:
#         if char in char_count:
#             char_count[char] -= 1
#             print(char_count)  
#             if char_count[char] == 0:
#                 del char_count[char] 
                
#         else:
#             return False 
      

#     return len(char_count) == 0  


# print(isAnagram("anagram", "nagaram"))  



word = "murali"
word_2 = "umaril"
char_map = {}
char_map2 = {}

for char in word: #5times len(word)=O(n)
    char_map[char] = char_map.get(char, 0) + 1

for char in word_2: #len(word_2)=O(m)
    char_map2[char] = char_map2.get(char,0) +1    

print(char_map == char_map2)
1+1+1+1+O(n)+O(m)+O(m)
0(m+n)