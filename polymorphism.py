class Animal:
    def __init__(self):
        pass

    def speak(self):
        print("I am an animal and I can speak")

class Dog(Animal):
     def __init__(self):
         pass

     def speak(self):
         print("I am a dog and i bark")

class Cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        print("I am a cat and i meow")


dog1=Dog()
dog1.speak()

cat1=Cat()
cat1.speak()
