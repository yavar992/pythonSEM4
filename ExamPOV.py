# diff b/w / nd // 
a =4
b =4
# true division
print(a/b) 
# floor division
print(a//b) 

# precende -- precendce determines the order in which the operators are performed in an expression that contain multiple operators
# ex --
# Precedence refers to the priority or order in which operations are performed in an expression that contains multiple operators. 
# Operators with higher precedence are evaluated before operators with lower precedence.

result = 2 + 3 * 4
print(result)
result = 2 + (3 * 4)  # result is 2 + 12, which equals 14
print(result)

# Associativity determines the order in which operators of the same precedence level are evaluated. Operators can be left-associative or right-associative:
# Left-Associative: Operators are evaluated from left to right.
# Right-Associative: Operators are evaluated from right to left.

result = 10 - 4 - 3
# Subtraction (-) is left-associative, so the expression is evaluated as:
result = (10 - 4) - 3  # result is 6 - 3, which equals 3
# For a right-associative operator example, consider the exponentiation operator (**):
result = 2 ** 3 ** 2
a=3
b=5, 
c=10
# print(a & b<2/5**2+c^b) 


# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = range(100) 
# range data types are used for defining the number or letter in a range

#display x:
print(x)
for i in range(100):
    print(i)


#Q4 How memory is managed in python? Explain PEP8? ---------------------

#  How is Memory Managed in Python? Explain PEP 8
# Memory Management in Python
# Memory management in Python is automatic and handled by the Python interpreter, which takes care of allocating and freeing up memory for your programs. Here’s how it works:

# Memory Allocation:

# Python uses a private heap to store objects and data structures. When you create a variable, Python automatically allocates memory for it in this heap.
# The memory manager in Python is responsible for keeping track of this heap and ensuring that there’s enough space for new objects.
# Reference Counting:

# Python keeps a count of how many references point to each object in memory. This is called reference counting.
# When an object’s reference count drops to zero (meaning no part of the program is using it anymore), Python automatically frees up the memory used by that object.
# Garbage Collection:

# Python also has a garbage collector to clean up memory that is no longer in use, particularly for objects involved in reference cycles (where two or more objects reference each other, preventing their reference counts from reaching zero).
# This garbage collector runs automatically in the background, helping to manage memory efficiently.
# Memory Pools:

# For small objects, Python uses memory pooling to reduce the overhead of frequent memory allocation and deallocation. This makes memory management more efficient.
# Overall, Python’s memory management is designed to be automatic and easy to use, so developers don’t need to manually manage memory like in some other languages.

# PEP 8 - Python’s Style Guide
# PEP 8 is a set of guidelines for writing clean, readable, and consistent Python code. Following PEP 8 helps you write code that’s easy to understand and maintain, especially when working in teams. Here are some key points from PEP 8:

# Indentation:

# Use 4 spaces per indentation level. This helps keep code blocks clear and easy to read.
# Avoid using tabs; stick to spaces for consistency.
# Line Length:

# Limit your lines to 79 characters. This makes your code easier to read on different screens and when using side-by-side windows.
# Blank Lines:

# Use blank lines to separate functions, classes, and sections of code within a function. This visually breaks up the code and makes it easier to follow.
# Imports:

# Group imports into three categories: standard library imports, third-party imports, and local imports. Keep each group separated by a blank line.
# Example:
# python
# Copy code
# import os
# import sys

# import numpy as np

# from mymodule import myfunction
# Naming Conventions:

# Use lowercase with underscores for variable and function names (e.g., my_variable).
# Use CamelCase for class names (e.g., MyClass).
# Use all uppercase letters for constants (e.g., MAX_SIZE).
# Whitespace:

# Use a single space around operators and after commas to keep your code clean (e.g., a = b + c, not a=b+c).
# Avoid extraneous spaces inside parentheses, brackets, or braces.
# Comments:

# Write comments that explain the why and how of your code, not just the what.
# Use docstrings for functions and classes to describe what they do.
# Consistency:

# Consistency is key in writing readable code. Stick to a style, whether it’s from PEP 8 or another agreed-upon standard.

# By following PEP 8 (Python Enhancement Proposal 8), you’ll write code that’s easier to read, understand, and maintain, 
# which is especially important when working with others or contributing to open-source projects




# How is Python Source Code Converted into Executable Code -------------------------------------------

# The Python source code goes through the following to generate an executable code

# Step 1: The Python compiler reads a Python source code or instruction in the code editor. In this first stage, the execution of the code starts.
# Step 2: After writing Python code it is then saved as a .py file in our system. 
# In this, there are instructions written by a Python script for the system.
# Step 3: In this the compilation stage comes in which source code is converted into a byte code. Python compiler also checks the syntax error in this step and generates a .pyc file.
# Step 4: Byte code that is .pyc file is then sent to the Python Virtual Machine(PVM) which is the Python interpreter. 
# PVM converts the Python byte code into machine-executable code and in this interpreter reads and executes the given file line by line.
#  If an error occurs during this interpretation then the conversion is halted with an error message.
# Step 5: Within the PVM the bytecode is converted into machine code that is the binary language consisting of 0’s and 1’s. 
# This binary language is only understandable by the CPU of the system as it is highly optimized for the machine code.
# Step 6: In the last step, the final execution occurs where the CPU executes the machine code and the final desired output will come as according to your program.



# TUPLES-------------------------

''' Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.'''
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
t1  = ("apple",)
print(type(t1))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Check if Item Exists
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple"  in thistuple :
    print("Item Exists")
    if "yavar" not in thistuple:
        print("yavar not found")

# as we know that we cannot modify the tuples ,  bt there is workaround we can change the tuples into the list and then we can change the list 
# and then we can change the list into tuples

ab = list(thistuple)
print(ab)
print(type(ab))
ab.pop(3)

newTuple = tuple(ab)
print(newTuple)

tuple1 += thistuple
print(tuple1)

# Unpacking a Tuple ----------------------------------------------------------------
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(red , yellow , pink) = fruits

print(red)
print(yellow)
print(pink)

# The number of variables must match the number of values in the tuple, if not, 
# you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

for i in range(len(fruits)):
    print(fruits[i])

for x in fruits:
    print(x)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3*3)






# Python Sets ----------------------------------------------------------------
# A set is a collection which is unordered, unchangeable*, and unindexed

thisset  = {1,2,4,5,"hello " , True , False , "hi" , 2,3,4 , 0.4 } # type: ignore
print(thisset)
# Sets are unordered, so you cannot be sure in which order the items will appear
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key..

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# Python Dictionaries ----------------------------------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# this is called obj in java
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

print(thisdict["model"])


# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Items - Data Types

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

x = thisdict.get("year")
print(x)

print(thisdict.keys())
print(thisdict.values())


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)




  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#   2 Define the term list comprehension. Write a python program to add an item in a tuple
# [new_element for element in iterable if condition]
'''
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or range).
List comprehensions are typically used to create a new list by applying a transformation or filtering elements from an existing iterable.
'''
list = [1,2,3,4,5,6,7,8,9,9,0,0]
squareList = [x**2 for x in list]
print(squareList)

dividerOf5 = [i for i in range(50) if i%5==0]
print(dividerOf5)




# Discuss the different types of argument passing methods in python. Explain the variable length argument  with any suitable example
# 1. Positional Arguments
# Definition: The most common type of argument passing. Arguments are passed to the function in the order in which they are defined


def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 30)  # Output: Hello, Alice. You are 30 years old.


#  Keyword Arguments
# Definition: You can pass arguments to a function by explicitly stating the name of the parameter and its value, regardless of their order in the function definition.


def greet(name , age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=43, name="yavar")


# Default Arguments
# Definition: In a function definition, you can provide default values for certain parameters. 
# If the caller does not provide a value for those parameters, the default value is used.

def greet(name, age=25):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice")  # Output: Hello, Alice. You are 25 years old.
greet("Bob", 30)  # Output: Hello, Bob. You are 30 years old.

# 4. Variable-Length Arguments
# Variable-length arguments allow you to pass a varying number of arguments to a function. There are two types:

# *args: For non-keyword variable-length arguments.
# **kwargs: For keyword variable-length arguments.

''' 
Variable-length arguments allow you to pass a varying number of arguments to a function. There are two types:
*args: For non-keyword variable-length arguments.
**kwargs: For keyword variable-length arguments
'''

'''
*args is used in function definitions to allow the function to accept a variable number of positional arguments. The *args syntax allows you to pass a collection of arguments to a function, which will be received as a tuple.
Simple Explanation:
Imagine you want to create a function that can take any number of arguments (not just a fixed number like 2 or 3). You use *args to collect all these extra arguments into a tuple, so you can work with them inside the function.
'''

def greet(*name):
   for names in name:
      print(f"hello {names}")

greet("yavar","ali","khan")      


'''
Keyworded Arguments (**kwargs)
**kwargs is used in function definitions to allow the function to accept a variable number of keyword arguments (arguments passed by name).
 The **kwargs syntax collects these keyword arguments into a dictionary.

Simple Explanation:
When you want to pass a bunch of named arguments (like key=value pairs) to a function, but you don't know in advance how many or which ones, you can use **kwargs.
 The function then receives these arguments as a dictionary, where the keys are the argument names and the values are the argument values.
'''

def greet(**kwargs):
   for key , value in kwargs.items():
      print(f"key:{key} value:{value}")


greet(name="yavar", age=32 , coutry="indiaa")