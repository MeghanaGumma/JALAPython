# 1. Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students={101: "Wendy", 102: "Solar", 103: "Joy", 104: "Seulgi", 105: "Yeri"}
print("Initial Dictionary: ",students)

# 1.1. Adding the values in dictionary
students[106]="Minnie"
print("After Adding a Value: ",students)

# 1.2. Updating the values in dictionary
students[102]="Irene"
print("After Updating a Value: ",students)

# 1.3. Accessing the value in dictionary
name=students[103]
print("Student ID 3: ",name)

# 1.4. Create a nested loop dictionary
nestedstd={
     101: {"name": "Jeongyeon", "age": 20},
     102: {"name": "Jihyo", "age": 21},
     103: {"name": "Chaeyoung", "age": 22}}
print("Nested Dictionary: ", nestedstd)

# 1.5. Access the values of nested loop dictionary
age=nestedstd[102]["age"]
print("Student ID 102 Age: ",age)

# 1.6. Print the keys present in a particular dictionary
keys=students.keys()
print("Keys: ",keys)

# 1.7. Delete a value from a dictionary
del students[104]
print("After Deleting a Value: ",students)

