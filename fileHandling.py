# craeting file

file=open("sample.txt","w")
file.write("This is a sample text file\n")
file.write("Another line in the file\n")  

# closing file is essential
file.close()
print("file creation is completed !")


# Reading file 

file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

# appending into  existing file

file=open("sample.txt","a")
file.write("New line appended \n")
file.close()
print(content)

file=open("sample.txt","r")
content=file.read()
print(content)
file.close()


## using with statement

with open("sample.txt","r") as file:
    content=file.readlines()
    for line in content:
        print(line.strip())