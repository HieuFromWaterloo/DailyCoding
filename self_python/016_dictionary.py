## Dictionary ##

my_dict = {"name": "Hieu Nguyen", "school": "Waterloo", "bank": 1000000}
print(my_dict)  # {'school': 'Waterloo', 'name': 'Hieu Nguyen', 'bank': 1000000}


# update({dict})
my_dict.update({"name": "Hoa Nguyen"})
print(my_dict)  # {'school': 'Waterloo', 'name': 'Hoa Nguyen', 'bank': 1000000}

my_dict.update({"name": "Hieu Nguyen", "bank": 2000000})
print(my_dict)

# pop() : my_dict.pop("school") OR del my_dict["age"]

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# SORTING
dict2 = {"Hien": 1, "Dung": 2, "Hieu": 3, "Hoa": 4}
# print(dict2[0])

# sort by key
sort_dict2 = sorted(dict2.items(), key=lambda k: k[0])
print(sort_dict2)

# sort by value
sort_dict2 = sorted(dict2.items(), key=lambda k: k[1])
print(sort_dict2)

print("Hien" in dict2)  # in ONLY works with keys
print(1 in dict2)
