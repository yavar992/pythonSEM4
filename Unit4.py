# FILE HANDLING

# BASIC STEPS IN FILE HANDLING/

# Opening a File: You need to open a file before you can read from or write to it.
# Reading/Writing: After opening a file, you can perform actions like reading its content or writing new content to it.
# Closing a File: After you’re done with the file, you should close it to free up system resources.


# 1. Opening a File
# You use the open() function to open a file. The open() function requires at least one argument: the file name.
#  It also takes a second optional argument that tells Python what you want to do with the file (read, write, etc.).

# file = open('.example.txt', 'r')
'''
Modes:
"r": Read mode (default) - Opens the file for reading.
"w": Write mode - Opens the file for writing (creates a new file or overwrites an existing file).
"a": Append mode - Opens the file for writing but appends to the end instead of overwriting.
"b": Binary mode - Used for non-text files like images or executables.
'''


# OPENING A FILE
# f = open("sample.txt" , "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#  if i try to execute the code without commenting the above code then i will get the blank lines as output becasue of read fun have already 
# read all the data of the files 

# readline -- read the data line by line in a file 
# data1 = f.readline()
# print(data1)

# data2 = f.readline()
# print(data2)

# f.close()

# the simple diff b/w the read and the readline is that read fun reads the whole file and readline fun reads the file line by line 


# write the data in file

# f = open("sample.txt" , "w")

# data = f.write("hello this is the new data being insert into the file ")
# when we open the file into the write mode and write something into the file ...then we actually overwrite the data in the file ...this delete old data inside the file
# and write the new data that we just inserted into the file


# before appending the data to the current file first of all we have to open the file in the append mode , by doing this we can append the data to the current file
# append() solve this issue ..append() insert the data to the current file that we are working in .. and doesn't delete the old data 

# f = open("sample.txt" , "a")
# data  = f.write("\n hope you guys are doing well in your life  ")
# f.close()


# if we opened the file in the append or write mode nd if the file doesn't exist then python will automarically make a new file in the same working direcotry
# example:

# f = open("demo.txt","w")

# f.close()


a = open("Sample.txt","r")
data = a.readlines()
# readlines reads all the lines in the file and returns a the file data as a list seperate by the line , each line in the file behave as a list item

print(data)
a.close()


# when we open the file in the write mode it truancate all the data present inside the file

# writelines()
# writelines() method in python is used to write the sequence of data like (list , tuples) inside the file rather than just write a sinlge line using the 
# write() method , by using the writeslines we can write the multiples lines in the file at once
#  ---------------------here is the example------------------

linesToWrite = ["hi this is yavar khan \n" , "i belong to the delhi\n" , "and currently i am persuing the python"]
f = open("demo1.txt","w")
data = f.writelines(linesToWrite)

f.close()

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

import os
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else :
    print("could not find demo.txt") 



# The seek() function in Python is used to change the current position of the file pointer within a file. This allows you to control where you start reading or writing in a file.
#  The file pointer is like a cursor that indicates your current position within the file's content.

with open("sample.txt", "r") as file:
    file.seek(14)
    content = file.read()
    print(content)



f = open("sample.txt", "r")

f.seek(4)
data = f.read()
print( "this is the content line " , content)
print(data)
# seek funtion in python used for changing the current postion of the file pointer within a file ...this allows us to control where we want to read or write
