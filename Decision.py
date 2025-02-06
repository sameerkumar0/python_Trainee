# if,elif and else

## if 

# a=int(input("enter a number"))

# if a>0:
#     print(f"number {a} is greater then 0 ")
# else:
#     print("please provide number greater than 0")


# odd even
# if a%2==0:
#     print(f"{a} is even number ")

# else:
#     print(f"{a} is odd number ")



# a= int(input("enter a number "))
# b= int(input("enter a number "))

# if a>b:
#     print("a is greater than b ")
# elif a==b:
#     print("a is equal to b ")

# else:
#     print("a is less than b ")



# lst=[]

# for i in range(2200,5001):
#     if (i%2==0) and (i%5==0):
#         lst.append(str(i))
# print(','.join(lst))



# start=int(input("enter a number "))
# end=int(input("enter a number "))

# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)


# a=0
# while a<7:
#     print("the number of sequence is",a)
#     a+=1

# n=int(input("enter thr number "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()



# for i in range(1,21):
#     if i%2==0:
#         print("odd number: ",i)


# for i in range(1,15):
#     if i==7:
#         break
#     print(i)


# a=10
# b="12"
# print(id(a))
# print(id(b))



# def sum(x,y):
#     return x+y

# print(sum(4,8))

# dictionary methods

# Dict={
#     "name":"ABC",
#     "age":22
# }

# # Dict.clear()
# Dict["phone no"]=8754872000
# print(Dict.keys())
# print(Dict.values())

# D2=Dict.copy()
# print(D2)

# D2.pop("name")
# D2.update({"address":"xyz"})
# print(D2)


# c=D2.get("age")
# print(c)


#tuple methods
# a = [10, 20, 30, 40, 50, 40, 60, 40, 70]

# # Find the index of 40 between index positions 4 and 8
# res = a.index(40, 6, 8)
# print(res)


# c=a.count(40)
# print(c)



#list 

# a=[5,6,1,2,3,45,7,8,5]
# # a.sort()
# print(a[2:5])


# b=["apple","banana","kiwi"]
# b.sort(key=len)

# print(b)


# #append

# c=[]

# c.append(12)
# c.insert(0,5) # add element at specific location
# c.extend([4,5,9,7])  # add multiple elemenets 
# c[1]=15   # update element present at location 1 
# print(c)




# t=2,1,45
# print(type(t))


# txt = "banana"

# x = txt.center(20, "-")

# print(x)


# a="agvd"
# print(a.upper())
# print(a.capitalize())



# a=input("enter the string :")

# if a==a[::-1]:
#     print(f"{a} is a palindrome")
# else:
#     print("Not a palindrome")



## decision making (if ,elif and else)

# a=int(input("Enter a number "))
# if a>0:
#     print("given number is positive ")
# elif a<0:
#     print("given number is negative ")
# else:
#     print("Given number is Zero ")


# odd even
# a=int(input("Enter a number "))
# if a%2==0:
#     print("number is even ")
# else:
#     print("Number is odd")



## vote eligibility

# age=int(input("Enter the age :"))
# if age>=18:
#     print("You are eligible to vote ")
# else:
#     print("You are not eligible to vote ")


##largest of two number

# a=int(input("enter first number :"))
# b=int(input("enter second number :"))

# if a>b:
#     print("a is lagest")
# elif a<b:
#     print("b is the largest ")
# else:
#     print("both are equal ")


#divisible by 5 and 7 

# a=int(input("enter a number :"))

# if (a%5==0) and (a%7==0):
#     print("given number is divisible by both (5 and 7) ")
# elif (a%5==0) and (a%7!=0):
#     print("given number is only divisible by 5 ")
# elif (a%7==0) and (a%5!=0):
#     print("given number is only divisible by 7 ")
# else:
#     print("given number is not divisible by 5 and 7 ")

#leap year

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# classify vowel
# a=input("enter a character :").lower()
# vowels="aeiou"
# if a in vowels:
#     print("it is a vowel ")
# else:
#     print("it is a consonet")


# valid triangle

# side1=int(input("enter a side :"))
# side2=int(input("enter a side :"))
# side3=int(input("enter a side :"))
# if side1+side2+side3==180:
#     print("its a valid traingle ")
# else:
#     print("not a valid triangle")

   

# Loops

# for i in range(1,11):
#     print(i)


# a=1
# while(a<=10):
#     print(a)
#     a+=1


# for i in range(1,21):
#     if i%2==0:
#         print(f"even number {i}")


# sum of first 10 natural number
# sum_nn=sum(range(1,11))
# print(sum_nn)


# sum_nn=0
# for num in range(1,11):
#     sum_nn+=num
# print("Sum:", sum_nn)


# using while loop
# sum_nn = 0
# num = 1
# while num <= 10:  
#     sum_nn += num
#     num += 1
# print("Sum:", sum_nn)


# table multiplication

# n=int(input("enter a number : "))
# for i in range(1,11):
#     print(f"{n} X {i} =",n*i)


# for i in range(1,6):
#     print("*"*i)

# for i in range(5,0,-1):
#     print("*"*i)


# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()


# for i in range(5):
#     for j in range(i-1,4):
#         print("*",end="")
#     print()


# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()


i = 2
while i <= 20:
    print(i,end=",")
    i += 2
