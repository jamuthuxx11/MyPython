#creating a dictionary
#data is stored in key value pairs
# ie key:value
"""
cardata={
    "model":"BMW",
    "year":2016,
    "brand":"c200"
}

print(cardata["brand"])# accessing values in a dictionary we use the key
cardata["alloys"]="contains" #addingdata to a dictionary
print(cardata)

cardata["brand"]="c500" #modifying data in a dictionary
print(cardata)
"""
#write a program that deletes a list of keys in a dictionary
# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_remove = ['a', 'c']
for key in keys_to_remove:
    del my_dict[key]

print("dictionary after removing keys:",my_dict)

#adding two lists in dictionarys
list1=["subaru", "bmw", "volkswagen"]
list2=["supra", "v8" ,"discovery"]
list3=dict( zip(list1, list2))
print(list3)
