#printing practice

    Here are some ways to **print a hashmap (dictionary) in Python** for practice.

---

### **1. Simple Printing**
```python
char_count = {'a': 3, 'b': 2, 'c': 1}
print(char_count)
```
**Output:**
```
{'a': 3, 'b': 2, 'c': 1}
```

---

### **2. Printing Keys and Values Separately**
```python
char_count = {'a': 3, 'b': 2, 'c': 1}

# Print only keys
print("Keys:", char_count.keys())

# Print only values
print("Values:", char_count.values())

# Print keys and values together
print("Items:", char_count.items())
```
**Output:**
```
Keys: dict_keys(['a', 'b', 'c'])
Values: dict_values([3, 2, 1])
Items: dict_items([('a', 3), ('b', 2), ('c', 1)])
```

---

### **3. Printing Using a Loop**
```python
char_count = {'a': 3, 'b': 2, 'c': 1}

for key in char_count:
    print(f"Key: {key}, Value: {char_count[key]}")
```
**Output:**
```
Key: a, Value: 3
Key: b, Value: 2
Key: c, Value: 1
```

---

### **4. Using `.items()` in Loop (Recommended)**
```python
char_count = {'a': 3, 'b': 2, 'c': 1}

for key, value in char_count.items():
    print(f"{key}: {value}")
```
**Output:**
```
a: 3
b: 2
c: 1
```

---

### **5. Printing in Sorted Order**
```python
char_count = {'b': 2, 'c': 1, 'a': 3}

for key in sorted(char_count):
    print(f"{key}: {char_count[key]}")
```
**Output:**
```
a: 3
b: 2
c: 1
```

---

### **6. Pretty Printing (Formatted Output)**
```python
import json

char_count = {'a': 3, 'b': 2, 'c': 1}

print(json.dumps(char_count, indent=4))
```
**Output:**
```
{
    "a": 3,
    "b": 2,
    "c": 1
}
```

---

### **7. Printing HashMap While Modifying It**
```python
char_count = {}

s = "banana"
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
    print(f"After adding '{char}': {char_count}")
```
**Output:**
```
After adding 'b': {'b': 1}
After adding 'a': {'b': 1, 'a': 1}
After adding 'n': {'b': 1, 'a': 1, 'n': 1}
After adding 'a': {'b': 1, 'a': 2, 'n': 1}
After adding 'n': {'b': 1, 'a': 2, 'n': 2}
After adding 'a': {'b': 1, 'a': 3, 'n': 2}
```

---

### **Practice Task**
Try running this:
```python
word = "murali"
word_2 = "umaril"
char_map = {}

for char in word:
    char_map[char] = char_map.get(char, 0) + 1

print("Final HashMap:", char_map)
```
💡 **Can you modify it to print the characters in alphabetical order?** 😊