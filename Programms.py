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
    
def primes_between(start, end):
    primeNumber = []
    for i in range(start , end+1):
        if(prime(i)):
         primeNumber.append(i)
         return primeNumber    



number = 24
if prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")        


list = [1,3,4,5,6,6]

for i in list:
    if i==3:
        continue
    print(i)


     # check if the year is leap or not

def isLeap(year):
    if(year%4==0 and year%100!=0) or ( year%400==0):
        return True
    else :
        return False    
    
year = 2000
if isLeap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




# calculated a programm to reverse a number

def reverseAnum(num):
    reversedNum = 0
    while(num>0):
        digit = num%10
        # Get the last digit
        reversedNum = reversedNum*10+digit
        # Append it to the reversed number
        num = num//10

    return reversedNum  



print(reverseAnum(456))


# pytoon program that accept a sentance and return the upparcase , lowercase and number

def countChar(str):
    upparCase = 0
    lowerCase = 0
    digit = 0
    for char in str:
        if char.isupper():
            upparCase += 1
        if char.islower(): 
            lowerCase += 1
        if char.isdigit():
            digit += 1

        return upparCase , lowerCase , digit             
    

sentence = str(input("ENTER A SENTNCE"))

uppar , lower , digit = countChar(sentence)

print(f"upparcase letter : {uppar}")
print(f"lowercase letter : {lower}")
print(f"digit letter : {digit}")



def count_characters(sentence):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for char in sentence:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    return uppercase_count, lowercase_count, digit_count

# Example usage
sentence = input("Enter a sentence: ")

uppercase_count, lowercase_count, digit_count = count_characters(sentence)

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")


