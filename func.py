# def greet(name):
#     print (f"hello ,{name}")
# greet("abs")


# def add(a,b):
#     return a+b
# result=add(5,7)
# print(result)


# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n=int(input("enter a number :"))
# print(fact(n))



# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(1, 2, 3, 4, 50))  



# #lambda function

# add=lambda x:x+x
# print(add(4))


# evenOdd = lambda x: "Even" if x % 2 == 0 else "Odd"
# x=int(input("enter number:"))
# print(evenOdd(x))

# #local scope
# def func():
#     x=10
#     print(x+5)

# func()




# # fibonacci
# def fibbo(n):
#     if n <= 0:
#         return "Invalid input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
    
#     a, b = 0, 1
#     for _ in range(n - 2):
#         a, b = b, a + b
#     return b

# n = int(input("Enter a positive number: "))
# print(f"The {n}-th Fibonacci number is: {fibbo(n)}")

# #fibonacci series

# def fibo_series(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# n = int(input("Enter number of terms: "))
# fibo_series(n)


# x=25  # global scope

# def func():
#     x=10 # local scope
#     print(x)

# func()
# print(x)

# #  check anagram
# from collections import Counter

# def IsAnagram(s,t):
#     if len(s) != len(t):
#         return False
#     s_dict=Counter(s)
#     t_dict=Counter(t)
#     return s_dict==t_dict
# s=input("enter string : ")
# t=input("enter string : ")
# print(IsAnagram(s,t))




fruits = ["apple", "banana", "cherry"]
for index,fruit in enumerate(fruits,start=1): # start define the starting point on index
    print(index,fruit)

index_name=list(enumerate(fruits,start=1))
print(index_name)