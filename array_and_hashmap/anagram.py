class solution:
    def isanagram(self, word:str, word_2:str)->bool:
        if len(word) != len(word_2):
            return False

        char_map = {}
        for char in word:
            char_map[char] = char_map.get(char, 0) + 1

        for char in word_2:
            if char not in char_map or char_map[char] == 0:
                return False
            char_map[char] -= 1
        return True

sol = solution()
print(sol.isanagram("anagram","naagram"))
     





