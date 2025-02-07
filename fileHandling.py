# write into file 

# file=open("example.txt","w")
# file.write("hello ! this is a demo file\n Demo text")
# file.close()

# # read file 
# file =open("example.txt","r")
# content=file.read()
# print(content)
# file.close()

# # read line
# file=open("example.txt","r")
# line1=file.readline()
# print(line1)
#file.close()

# # read all line
# file=open("example.txt","r")
# lines=file.readlines()
# print(lines)
#file.close()


# append into existing file

# file=open("example.txt","a")
# file.write("this is new line\n")
# file.close()

file=open("example.txt","r")
content=file.read()
print(content)
file.close()
