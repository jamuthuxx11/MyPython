mystudents=["ethan","james","franko",]
print(mystudents)
#append used to add sth to a list
mystudents.append("daisy")
print(mystudents)
#remove used to remove someone from the list
mystudents.remove("ethan")
print(mystudents)
#modifying the list
mystudents[1]="franko100"
print(mystudents)
#creating an empty list then adding to the list
fruits=list()
fruits.append("apple")
fruits.append("avocado")
fruits.append("pineapple")
print(fruits)


#version 1 quiz
mystudents=list()
for x in range(3):
    student=input("enter student name:")
    mystudents.append(student)
print("list of students:",mystudents)
