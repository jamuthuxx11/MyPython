#exception handling
y =20

try:
    if y>20:
            print("the number is greater than 20")
    else:
        print("the number is less than 20")
except Exception as e :
    print("error:,e")
print("program ended")


try:
    x=20

    print(x/y)
except Exception as e:
    print("error:,e")
    
