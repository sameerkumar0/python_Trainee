# # craeting file

# file=open("sample.txt","w")
# file.write("This is a sample text file\n")
# file.write("Another line in the file\n")  

# # closing file is essential
# file.close()
# print("file creation is completed !")


# # Reading file 

# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()

# # appending into  existing file

# file=open("sample.txt","a")
# file.write("New line appended \n")
# file.close()
# print(content)

# file=open("sample.txt","r")
# content=file.read()
# print(content)
# file.close()


# ## using with statement

# with open("sample.txt","r") as file:
#     content=file.readlines()
#     for line in content:
#         print(line.strip())


# # writting multiple lines
# lines=["Add line one\n","Add line two\n"]
# with open("sample.txt","w") as file:
#     file.writelines(lines)
# print("lines added succesfully :")



# import os 

# filename="sample.txt"
# if os.path.exists(filename):
#     with open("sample.txt","r") as file:
#         print(file.read())
# else:
#     print("file not found :")


# # writting Csv file
# import csv

# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 25, "New York"],
#     ["Bob", 30, "London"],
#     ["Charlie", 22, "Paris"]
# ]

# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("CSV file created!")


# with open("people.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



# working with binary format

text="hello ,binary conversion"

with open("binary.bin","wb") as file:
    file.write(text.encode("utf-8"))
print("converted to binary :")  


# Reading binary data and converting to text
with open("binary.bin", "rb") as file:
    binary_data = file.read()  
    # text = binary_data.decode("utf-8")  

print(binary_data)
