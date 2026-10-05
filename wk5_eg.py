students = {
    "S001": "Alice",
    "S002": "Bob",
    "S003": "Charlie"
}

print(students.keys())

for key, value in students.items():
    print(key, value)


import json

students = [
    {"name": "Ali", "mark": 75},
    {"name": "Sara", "mark": 88}
]

# Read Data
for student in students:
    print(student["name"])

# Update Data
students[0]["mark"] = 80

# Add (Create) Data
students.append({
    "name": "John",
    "mark": 65
})

# Save JSON File
with open("students.json", "w") as f:
    json.dump(students, f)