def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False  # If lengths are different, they can't be anagrams

    char_count = {}

    # Count characters in `s`
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrease count for characters in `t`
    for char in t:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]  # Remove character if count reaches zero
        else:
            return False  # Extra character in `t`

    return len(char_count) == 0  # If all counts are zero, it's an anagram

# Example cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
