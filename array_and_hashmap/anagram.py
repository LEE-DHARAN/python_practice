class solution:
    def isanagram(self, word_1:str, word_2:str)->bool:
        if len(word_1) != len(word_2):
            return False

        char_map = {}
        for char in word_1:
            char_map[char] = char_map.get(char, 0) + 1

        for char in word_2:
            if char not in char_map or char_map[char] == 0:
                return False
            char_map[char] -= 1
        return True

sol = solution()
print(sol.isanagram("anagram","naagram"))
     





