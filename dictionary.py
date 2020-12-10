d = {"chandler": 10924378, "joey": 12945543, "monica": 54346275, "phoebe": 32398476}

print(d)

d["rachel"] = 82398473      # adds a nex entry

print(d)

del d["monica"]             # deletes an entry from the dictionary

print(d)

for key in d:
    print("Name: ", key, "Phone number: ", d[key])      # 1st method of writing a for loop for a dictionary


for k, v in d.items():                                   # 2nd method of writing a for loop for a dictionary
    print("Name: ", k, "Phone number: ", v)

d.clear()                                               # deletes all the values
