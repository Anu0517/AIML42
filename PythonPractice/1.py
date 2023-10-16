name = "Anushka"
age = 18
print(name)
print(age)
#True with a cap T

name1= "Tony"
name2= "Stark"
age = 51
is_genius = True
print("Name: "+name1 +name2)
print("Age:"+ str(age))
print("He iss genius:"+ str(is_genius))

name = input("What is your name? ")
print(name)

#type conversion
old_age = input("Enter your old age: ")
new_age = int(old_age) + 2
print(new_age)

#ADDING TWO NUMBERS
firstnum = input("Enter the first number: ")
secondnum = print("Enter second number: ")
sum = int(firstnum) + int(secondnum)
print("Sum"+str(sum))

#STRING METHODS
name = "Tony Stark"
print(name.upper())
print(name.lower())
print(name.find('S')) #returns the index of the value and blank also has a index
print(name.find('s')) #return -1
print(name.find('Stark')) #index of the first char that is S
print(name.replace("Tony Stark","Iron man"))
print(name)
print(name.replace('r','n'))
print("T" in name) #to see it the char or sub string that is Tony is there or not 

#AR OPERATOR
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3%2)
print(3**2) #3 to the power of 2
i=5
i += 2
i -= 2
i *= 2

#Comparision Oerator 
< , > , == , <= , >= , !=
Logical -> , or , and , not - acutal words no symbols
print(not 3==3)
print(3>2 or 3>4)
print(2==2 and 1==1)

#IF-ELSE STATEMENTS
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
elif age < 18 and age>3:
    print("You can't vote")
else:
    print("You are a child")
print("Thank You")  

#CALCULATER
a = int(input("Enter 1st number: "))
b = int(input("Enterr 2nd number: "))
print("Sum: " + str(a+b))
print("Rem: "+str(a-b))
print("Product: "+str(a*b))
print("Div: "+str(a/b))
print("Mod: "+str(a%b))

a = int(input("Enter 1st number: "))
op = input("Enter operator(+,-,*,/,%): ")
b = int(input("Enterr 2nd number: "))
if op=="+":
    print("Sum: "+str(a+b))
elif op=="-":
    print("Sub: "+str(a-b))
elif op=="*":
    print("Product: "+str(a*b))
elif op=="/":
    print("Div: "+str(a/b))
elif op=="%":
    print("Mod: "+str(a%b))
else:
    print("Invald Operation")

#range is a function in py

#LOOPS
#WHILE
i = 1
while i <=10000:
    print(i)
    i += 1
while i<=5 :
    print(i * "*") #patterns asked for placement 
    i += 1

#FOR
for i in range(5):
    print(i)

#LIST - collection of items - []
ma = [1,2,"math"]
print(ma)
print(ma[1])
print(ma[-1]) #counts backwards 
print(ma[0:2]) #only 0 and 1 will be included - 2 will not be included
for score in ma: #one by one 
    print(score)

#LIST METHODS/OPERATIONS
marks = [99,98,97]
marks.append(96)
print(marks)
marks.insert(0,100)
print(marks)
print(99 in marks)
print(len(marks))
i=0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()
print(marks)

#break and continue keyword
stu =["El","Mike","Dustin","Lucas","Max","Will"]
for student in stu:
    if student == "Will":
        break;
    print(student)'''
'''stu =["El","Mike","Dustin","Lucas","Max","Will"]
for student in stu:
    if student == "Lucas":
        continue;
    print(student)

#TUPLE - immutable list - () 
marks=(99,98,97,99)
print(marks.count(99))
print(marks.index(99))

#if {} or () or [] is missed then by default it will be a default 

#SET - {} - no index - unique value is stored - unordered
marks={99,98,97,99}
print(marks) #99 will be printed once - as a unique value is stored
#print(marks[0]) #error - as index does not exist

#DICTIONARY - unordered - info store in pairs - pairs of key and value
marks ={"English":99 , "Chemistry":98} #english is key and 99 is value
info = {"Will" : "Joyce" }
print(marks["English"]) #key is used to access the value
marks["Physics"]=97
print(marks)
marks["Chemistry"]=88
print(marks)

#FUNCTIONS 
'''1. In-Built - int(), str(), bool() etc
2.Module 
3.User-Defined ''' 

#2 - if related functions and related variables are stored in the same function it's called a module in py
import math #math is a module 
print(dir(math)) #prints all the math module functions
from math import sqrt #specific functions 
print(sqrt(4))
from math import *  #select all - all the functions

#3
'''Syntax:
def function_name(parameters):
    //block of code
def - defition - defining the function 
'''
def print_sum(first,second):
    print(first+second)
print_sum(1,2)   #calling the function

def print_sum(first,second=4):
    print(first+second)
print_sum(1)

'''
OOPS in Python - programming , placements , competative prgramming
Modules , File Handling - AI , DS , ML
Django - development'''
#Multi Line comment -> '''  ''' or """   """