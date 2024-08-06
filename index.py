print("hello")

if 5>2:
 print("5 is greater")
 print("5 i greater")


x =4
y = "yavar"
y = "anas"
print(y)

x , y , z = "a " , 5 , True
print(x)
print(y)
print(z)

x = y = z = "a"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x , y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

ab =5
bc =6

ab = ab+bc
bc = ab - bc
ab = ab-bc

print(ab , bc)

# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))

# num1 = num1+num2
# num2 = num1-num2 
# num1 = num1-num2
# print( "the swap numbers are  " , num1,num2)

txt = "The best things in life are free!"
print("free" in txt)

print("hi my name is yavar ali khan " , " i live in delhi")

# name = str(input("what is your name"))

# print("your name is " , name)

print("hello " + "yavar ali khan")
ab = 5.9
print(int(ab))

na = "2999"
print(int(na))

str1 = "yavar ali khan"
print(len(str1))
print(str1[2])
print(str1.find('i'))

age = 83

str = f"my uncle age is {age}"
print(str)

if 3>4 :
  print("13 is greater")

print(bool("Hello"))
print(bool(15))
print(bool(False))
print(bool("Hello"))
print(bool(True))

list = [ "Hello", "world" , "there " , "i" , "hello"]
list[1] = "duniya"
print(list[1])
print(list)
print(len(list))

list = ["hello",1 , True , 5.44 , {"hello":1 , "world":2 , "nice":3}]  
# a list can contain any type of data type in it 
print(list)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

for fruits in thislist :
  print(fruits)

list1 = ['M', 'o', 'n', 'k', 'y'] 
print("@".join(list1))


list2 = ["#4","4dw",5,5.5]

list1.extend(list2)

print(list1)

l = range(50)

for i in l:
  print(i)