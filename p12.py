student = {
    "name": "Amit",
    "roll": 101,
    "marks": 85
}

print("Dictionary:", student)
print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student["grade"] = "A"
print("After adding grade:", student)

student["marks"] = 90
print("After updating marks:", student)

del student["roll"]
print("After deleting roll:", student)
