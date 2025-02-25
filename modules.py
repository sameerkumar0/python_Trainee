
# math module
import math

print(math.pi)

# area of circle

r=4
pie=math.pi
print(pie*r*r)


x=2.5
y=4
print(math.ceil(x)) # prints upper bound
print(math.floor(x)) # prints lower bound
print(math.factorial(y))
print(math.gcd(84,48))
print(math.gcd(23,69))

print(math.sqrt(5))


# os module

import os 
cwd=os.getcwd()
print("current workin directory",cwd)


path = "/"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list) 


# random module

import random 
num=random.random()
print(num)

num1=random.randint(1,200)
print(num1)

num2=random.randrange(1,10)
print(num2)


list1 = [34, 23, 65, 86, 23, 43]    
random.shuffle( list1 )    
print( list1 )   


colors=["red","green","yellow","blue"]
print(random.choice(colors))


random.seed(42)
print(random.random())

import string
def generate_password(length=8):
    character=string.ascii_letters+string.digits
    return ''.join(random.choices(character,k=length))
n=int(input("Enter length of password you want :"))
print(generate_password(n))

def start_game():
    print("Enter your choice : ")
    print("Choice 1: Rock ")
    print("Choice 2: Paper ")
    print("Choice 3: Scissor ")
user_choice=int(input("Enter your chioce 1-3 : "))

choice_machine=random.randint(1,3)

# display the machines choice  
print(" Option choosed by Machine is: ", end = " ")  
if choice_machine == 1:  
    print(" Rock ")  
elif choice_machine == 2:  
    print("Paper")  
else:  
    print("Scissors")

# winner
if user_choice==choice_machine:
    print("its a tie ! ")
elif user_choice==1 and choice_machine==3:
    print("You won ")
elif user_choice==2 and choice_machine==1:
    print("You won ")
elif user_choice==3 and choice_machine==2:
    print("You won ")

else:
    print("Machine won the game ")  

play_again = input(" Want to Play again? ( yes / no ) ").lower()  
if play_again == " yes ":  
    start_game()  
else:  
    print(" Thanks for playing Rock-Paper-Scissors! ")  
start_game()

# Datetime Module

import datetime
from datetime import date
Today=date.today()
print(Today)
print(Today.month)
print(Today.year)
print(Today.day)

from datetime import datetime
Time=datetime.utcnow()
print(Time)