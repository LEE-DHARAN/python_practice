# ✅ Creating a HashMap (Dictionary)
student_marks = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3
}

# 🔍 Accessing values using keys
print(student_marks["Bob"])  # Output: 90

# ✏️ Adding a new key-value pair
student_marks["David"] = 88

# ❌ Checking if a key exists
if "Eve" in student_marks:
    print(student_marks["Eve"])
else:
    print("Eve not found")  # Output: Eve not found

# 🚀 Iterating through HashMap
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# 🗑️ Deleting a key
del student_marks["Charlie"]

print(student_marks)  # Output: {'Alice': 85, 'Bob': 90, 'David': 88}

