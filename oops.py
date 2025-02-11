class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
d1=animal("Dog",10)

d1.name="Cat"
print(d1.name)


class smartphone:
    # constructor
    def __init__(self,device,brand): # self is default parameter
        self.device=device
        self.brand=brand
    # method of class
    def decription(self):
        return f"{self.device } of {self.brand} supports android 14"


# object creation

phoneObj=smartphone("Mobile Phone","Samsung")
print(phoneObj.decription())



# encapsulation

class desktop:
    def __init__(self):
        self.__max_price=25000

    def sell(self):
        return f"selling price {self.__max_price}"
    
    def set_max_price(self,price):
        if price > self.__max_price:
            self.__max_price=price

# object

desktopObj=desktop()
# print(desktopObj.sell())

# modify the price directely (###this will not work )
desktopObj.__max_price = 35000
print(desktopObj.sell())


# modify the price  using stter function
desktopObj.set_max_price(30000)
print(desktopObj.sell())


# Inheritence

class Parent:
    parentAttr=100

    def __init__(self):
        print("parent class :S")

    def parentMethod(self):
        print("parent method :")

    def setattr(self,attr):
        Parent.parentAttr=attr
    
    def getattr(self):
        print("parent Attribute ",Parent.parentAttr)


# Child class 

class child(Parent):
    def __init__(self):
        print("child constructor :")

    def childMethod(self):
        print("child constructor :")

# instance of child

c=child()

# child method
c.childMethod()

#parent method
c.parentMethod()
c.setattr(500)

c.getattr()


# multiple inheritence

class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):  
    def method_c(self):
        print("Method C")

c = C()
c.method_a()  
c.method_b()  
c.method_c()  


class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal): 
    def speak(self):
        print("Dog barks")  

d = Dog()
d.speak()  


# Polymorphism
class Bird:
    def speak(self):
        print("Bird makes sound")

class Parrot(Bird):
    def speak(self):
        print("Parrot talks")

class Crow(Bird):
    def speak(self):
        print("Crow caws")

# Using polymorphism
for bird in [Parrot(), Crow()]:
    bird.speak()


class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Create object
car1 = Car("Honda", "Model vsi")
car1.display_info()  


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable(__ is used to define a private variable)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount(1000)
account.deposit(1500)
print(account.get_balance()) 


# Inheritence
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        return "Bark"
class cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
print(dog.speak())  

Cat=cat()
print(Cat.speak())



# str() (user friendly representation)

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f"{self.brand} {self.model}"
    
Car=car("Honda","Civic")
print(Car)


# __repr__ (developer friedly represntation)

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"
    
Car=car("Honda","Civic")
print(repr(Car))



# *args and **kwargs

def add_num(*args): # take multiple positional arguments and add that
    return sum(args)

print(add_num(2,30,3)) 

def name(*args):
    for name in args:
        print(name)

name("abc","xyzs")


