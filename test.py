# task 1
x=int(input("enter number: "))
print(x*2)

#task 2
def greet(name):
    print("Hello,", name)
    if name == "Alice":
        print("Welcome back!")
    print("Have a great day!")

greet("Alice")

#task 3

x = "5"
y = 2
print(int(x) + y)  # Line 1
print(x + str(y))  # Line 2
print(float(x) + y)  # Line 3


def square(n):
    return n*n

print(square(4))