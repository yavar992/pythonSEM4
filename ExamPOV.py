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
