list 

a=[4,5,6,7,8,9,5]
print(a)


#length of list without len() keyword
a=[4,5,7,5,6,8]
count=0
for _ in a:
    count+=1
print("length of list  is ",count)



a=[4,5,7,5,6,8]
print("length of list is:",len(a))

a=["apple","banana","cherry","mango"]
# for i in a:
#     print(i,end=",")
print(type(a))
   
#nested list
mat=[
    [1,5,5,7],
    [8,6,3,4],
    [5,6,2,4]
]

print(mat[1][1]) # accesing second row and second column element


#max element present in the list

a = [10, 24, 76, 23, 12]

print(max(a))


a=[10,25,45,30,7,90]

largest=a[0]
for val in a:
    if (val > largest):
        largest=val
print(largest)


a = [10, 20, 30, 40, 50, 40, 60, 40, 70]

#index of 40 between index positions 4 and 8
inde = a.index(40, 4, 8) # 4 start and 8 end parameter
print(inde)



#remove duplicate 
a=[2,5,2,4,6,7,8,9,5,1]

rem_duplicate=[]

for i in a:
    if i not in rem_duplicate:
        rem_duplicate.append(i)
rem_duplicate.sort()
print(rem_duplicate)

a=[2,5,2,4,6,7,8,9,5,1]
rem_duplicate=list(set(a))
print(rem_duplicate)


#count the accurance of the element in the list

a=[2,5,2,4,6,7,8,9,5,1]
# print(a.count(5))
a.sort()
a.reverse()
print(a)



#merge two list 
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merge=list1+list2
merge.sort() # sort the list 
print(merge)

num=[4,5,6,3]
sqare=list(map(lambda x:x**2,num))
print(sqare)



## tuple----

a=(2,)
print(type(a))



fruits = ("apple", "banana", "cherry","mango","kiwi")
print(fruits)
print(fruits[2]) # accesiing the 3rd elemenet

print(fruits[0:2]) # slicing a tuple
print("orange" in fruits)


a=(4,6,8,4,57,4,6,4)
print(len(a)) # len keyword is used to get the length of a tuple

#comman element in both tuple
t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

common = tuple(set(t1) & set(t2))
print(common) 


#tuple packing
name=("a","b","c")
age=(20,22,19)
combine=list(zip(name,age))
print(combine)




#dictionary

d={
    "name":"abc",
    "age":22,
    "phone":54216121
}

print(d)

#using dict() constrauctor

d1=dict(name="abs",age=21,)
d1["gender"]="male"
print(d1)
print(d1.get("phone")) #get is used to ignore the error when the element is ot present

for key in d1:
    print(key)

for value in d1.values():
    print(value)



#sets


fruits = {"apple", "banana", "cherry"}
# using set constructor
numbers = set([1, 2, 3, 4, 4, 5])  

print(fruits)    
print(numbers)   


#set methods 
s={5,6,2,4}
s.add(7) # add single value


s.update([9,3,1])# add multiple values
s.remove(1) # remove  value from set
print(s)


#set using range 
num=set(range(1,11))
print(num)


a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))  
print(b.issuperset(a))  

comb=[(x,y)for x in [1,2,3] for y in [3,4,5] if x!=y] #list comprehension
print(comb)

# zip function (combine the multiple iterable  into a single iterable )
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(names, ages)
print(list(zipped))

# using for loop
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


# nested tuple
t=1254,5464,'hello'
u=t,(5,6,87,'you')
print(u)


# set comprehension

a={x for x in 'abracadabra' if x not in 'abc'}
print(a)


# array min value

array=[7,5,6,98,45,14,52]
minVal=array[0]
for i in array:
    if  i< minVal:
        minVal=i
print("Lowest values is :",minVal)


# binary search 
def binary_serach(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right) //2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = int(input("enter target value :"))
result = binary_serach(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
