#creating a function in python
def is_even(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


#calling  a function
is_even(80)

#function 2
def printEmobilis():
    for i in range(10):
        print(i+1,"Emobilis")

printEmobilis()


#function 3
def printName(x):
    for i in range(2):
        print(x)


printName("jude")
printName("jamu")

#function 4
def getModulous(y,x):
    return y%x

z =getModulous(6,9)  +20

print(z)

def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [11,25,32,46,55,60,7,81,0]
largest_numbers = find_largest_number(numbers)
print("The largest number in the list:",largest_numbers)

def find_repeateditems(lst):
    count_dict = {}
    duplicates = []

    # Count occurrences of each element in the list
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1


    for item, count in count_dict.items():
        if count > 1:
            duplicates.append(item)

    return duplicates


my_list = [11, 2, 3, 4, 2, 58, 6, 11, 4]
print("Repeated elements in the list:", find_repeateditems(my_list))

#repeated elements version 2 using sets
fruits=["apple","banana","pawpaw","apple","banana","grape"]
myrepeated=set()
for item in fruits:
    if fruits.count(item) > 1:
        myrepeated.add(item)

print(myrepeated)

#repeated elements using lists
fruits2=["apple","banana","pawpaw","apple","banana","grape"]
myrepeated2=list()
for item in fruits2:
    if fruits2.count(item) >1:
        myrepeated2.append(item)

print(myrepeated2)
