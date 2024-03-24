#single line comment
"""
multiline comments
multiline comments
multiline comments
multiline comments
"""
#variables and the different data types
student_name= "Jamu" #string
student_age=19 #integer
student_height=6.4 #float
is_male=True #boolean

print("My students name is:",student_name)
print("My students age is:",student_age)
print(student_height)
#print(student_name,student_age,student_height)

firstname="name of the student"
secondname=150
fullname=firstname+" "+str(secondname)
print(fullname)


price1="300"
price2=700
total=int(price1)+price2
print(total)
#total=float(price1)+float(price2)
#print(total)

#operators
#arithmetic operators
# + - / % ** //
print(2%5)

#checking if a number is odd or even
#y=20
#print(y%10)
#if y%2==0:
    #print("even")
#else:
    #print("odd")






#Assignment operators
z=6
z+=4 #z=z+4
z%=5
print(z)

#COMPARISON OPERATORS
print(5!=2)
print(5==2)
print(6>7)
print(7<9)

#LOGICAL OPERATORS
# AND , OR
age=32
nationality="Nigerian"
if nationality=="Nigerian" and age==32:

    print("you can be MANAGER")
else:
    print("you can't be MANAGER")






#checking if a number is odd or even
"""
x=int(input("enter a number:"))
x=8
if x%2==0:
    print("even")
else:
    print("odd")
"""

#illustration of elif
#z=6
#if z>3:
 #   print("the value of z is more than 3")
#elif z==3:
 #   print("the value of z is equal to 3")
#else:
 #   print("the value of z is less than 3")

#checking city of candidate using elif
#city=input("enter city name:")
#if city=="Mombasa":
    #print("you are ABLE to become president")
#elif city=="Nairobi":
    #print("you are ABLE to become president")
#elif city=="Kisumu":
   # print("you are ABLE to become president")
#else:
#    print("you are NOT ABLE to become president")

#x=int(input("enter your first number:"))
#y=int(input("enter your second number:"))
#operation=str( input("enter your operation:"))
#if operation=="add":
 #   print(x+y)
#elif operation=="subtract":
  #  print(x-y)
#elif operation=="multiplication":
   # print(x*y)

#LOOPING
#x=1
#while x<=10:
  #  print("the value of x is:",x)
 #   x+=1
#print("success")

#continue and the break statement
#x=1
#while x<=10:
 #   if x==3:
  #      x+=1
  #      continue
   ##x+=1
#print("end of continue statement")

#Brake Statement
x=1
while x<=10:
    if x==3:
        x+=1
        break
    print(x)
    x+=1
print("end of break statement")\

y=2
while y<=7:
    print("the value of y is:",y)
    y+=1
else:
    print("loop ended")
"""
x=0
sum=0
while x<=10:
    if x%2==0:
        x=x+1
        continue
    else:sum=sum+x
    x=x+1
else:
    print(sum)

visitors=int(input("enter the number of visitors:"))
ugandan =0
kenyan=0
counter=1

while counter<=visitors:
    nationality = input("enter the nationality:")
    if nationality=="kenyan":
        kenyan+=1
        print("allowed")
        counter+=1
    else:
        ugandan+=1
        print("not allowed")
        counter+=1
"""
""""
print("the number of visitors is: ",visitors)
print("the number of kenyans is: ",kenyan)
print("the number of ugandans is:",ugandan )
"""
#for loop
names=["ETHAN","JAMU","MWAKIO"]
for names in names:
    print(names)

#while loop implimentation
names=["ETHAN","JAMU","MWAKIO"]
x=0
while x<len(names):
    print(names[x])
    x+=1
"""
for x in range(5):
    print("franko")
"""
"""
y=0
while y<4:
    print("franko")
    y+=1
"""
for x in range(2,4):
        print("franko")

for x in range(2,4,10):
          print("jamuh")
#sum of all even numbers btn 0-10 using while loop
sum=0
for x in range(1,11):
    if x%2==0:
        sum=sum+x
print("the sum is ",sum)