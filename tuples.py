#tuples
"""
my_tuple = ("jamu,","jude","jose")
print(my_tuple)
"""
#properties of turples
"""
1.turples are immutable ie.they cant be changed directly 
2.elemets in a tuple are indexed
3.tuples are usually in round brackets 
4.tuples are allow duplicates
5.tuples can have elements of different data types

"""
"""
print(my_tuple[1])
my_tuple[1] ="jamu"   #this will give an error because we cannot change tuples directly
print(my_tuple[1])
"""
#to modify/add/delete turples
"""
1.convert the tuple to a list
    mylist=list(the tuple name)
2.modify the value you wanted the same way we did in lists
    example on modification:
            student [0]="jamu"
    example on deleting:
            student.remove [0]="jude"
    example on adding:
            student.add=("jamu")
"""
#how to add an item in a tuple
original_tuple = (1,2,3,4,5)
print(original_tuple)

#item to add
new_item = (6,7,8)
print(new_item)
#creating new tuple by adding  item
new_tuple = original_tuple + (new_item,)

print("Original Tuple:",original_tuple)

print("New Tuple:",new_tuple)