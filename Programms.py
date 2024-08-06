# Parts of a Function
# Function Definition:

# Keyword: Functions are defined using the def keyword.
# Name: A function must have a unique name to identify it.
# Parameters: Functions can accept inputs, known as parameters, enclosed in parentheses.
# Colon (:): The function definition ends with a colon.
# Docstring (Optional): A string that describes the function, enclosed in triple quotes, and placed right after the function header.
# Body: The indented block of code under the function definition that contains the statements that execute when the function is called.
# Return Statement: The return statement specifies the value to be returned by the function. If not used, the function returns None by default.
# Explain with example (take simple calculator with add,  subtract, division and multiplication)

# Function for addition
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Function for subtraction
def sub(a, b):
    """Returns the difference between two numbers."""
    return a - b

# Function for multiplication
def mul(a, b):
    """Returns the product of two numbers.""" 
    return a * b

# Function for division
def div(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if a == 0:
        return "ERROR :  Division by zero"
    return a / b 

# Main code to demonstrate the functions
# Global variables
num1 = 10
num2 = 5

# Function calls
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {sub(num1, num2)}")
print(f"{num1} * {num2} = {mul(num1, num2)}")
print(f"{num1} / {num2} = {div(num1, num2)}")

print(f"the sum of {num1} + {num2} is + {add(num1, num2)}")




'''' 
Q6-- write a python function removekth(s,k) that takes as 
input a string a and an integer k>=0 and removes the 
character at index k. if k is beyond the length of s , the 
whole of s is returned for example
removekth(“python”, 1) return “pthon”
removekth(“python”, 3) return “pyton”
removekth(“python”, 0) return “ython”
removekth(“python”, 20) return “python”
 '''

def removekth(s,k):
    if k<=0:
        return "K must be greater than 0"
    if k>len(s):
        return s
    # BECASUE PYTHON USE THE 0 BASED INDEX
    indexToRemove = k-1
    word = list(s)
    word.pop(indexToRemove)
    return ''.join(word)

print(removekth("yavar",0))



list = [2,4,5,2,5,'dd',32]
print("length of list is " , len(list))

# word = "yavar"
# list = list(word)
# print(list)
# print(list.pop(3))
# print(''.join(list))
# join is the method of the string





# Q4 Any pattern question

# for i in range(6):  # From 0 to 5
#     for j in range(i + 1):  # Print i + 1 stars for each row
#         print('*', end='')  # Print '*' without new line
#     print()  # Move to the next line after each row


for i in range(0,6):
    for j in range(i +1):
        print("*" , end= '')
    print()   


#write a programm to find the prime number

def prime(num):
    for i in range(2, int(num**0.5) +1):
        if num%i==0:
            return False
        return True
    
number = 24
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")        
    