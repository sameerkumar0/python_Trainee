# class animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# d1=animal("Dog",10)

# d1.name="Cat"
# print(d1.name)


# class smartphone:
#     # constructor
#     def __init__(self,device,brand): # self is default parameter
#         self.device=device
#         self.brand=brand
#     # method of class
#     def decription(self):
#         return f"{self.device } of {self.brand} supports android 14"


# # object creation

# phoneObj=smartphone("Mobile Phone","Samsung")
# print(phoneObj.decription())



## encapsulation

# class desktop:
#     def __init__(self):
#         self.__max_price=25000

#     def sell(self):
#         return f"selling price {self.__max_price}"
    
#     def set_max_price(self,price):
#         if price > self.__max_price:
#             self.__max_price=price

# # object

# desktopObj=desktop()
# # print(desktopObj.sell())

# # modify the price directely (###this will not work )
# desktopObj.__max_price = 35000
# print(desktopObj.sell())


# # modify the price  using stter function
# desktopObj.set_max_price(30000)
# print(desktopObj.sell())


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
