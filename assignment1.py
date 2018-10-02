#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter the year"))
if(year%4==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input("Enter length"))
b=int(input("Enter breadth"))
if l==b:
    print("it is square")
else:
     print("it is Rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
x=int(input("Enter first age"))
y=int(input("Enter second age"))
z=int(input("Enter third age"))
if x>=y and x>=z:
    print("Oldest is",a)
elif y>=x and y>=z:
    print("Oldest is",b)
elif z>=x and z>=y:
    print("Oldest is",z)
else:
    print("All are equal")
     
     
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR". 
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
age=int(input("Enter age"))
sex=input("SEX? (M or F)")
marry=input("MARRIED? (Y or N)")
if sex == "F":
    print("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
    print("you can work anywhere")
elif sex == "M" and age>=40 and age<=60:
    print("Urban areas only")
else:
    print("ERROR")
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity=input("Enter quantity")
if quantity*100 > 1000:
    print("cost is",((quantity*100)-(.1*quantity*100)))
else:
    print("cost is",quantity*100)

#LOOPS
#Q.1- Take 10 integers from user and print it on screen. 
print(max((int(input("Enter a number: ")) for x in range(10))))
#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
print("infinite")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

m=list(map(int.input().split()))
m_square=[]
for i in 1:
    m_square.append(i**2)
print(m_square)
print('-'*5)
#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
list= [5,'a', 'b', 'c', l,'d', 3,9.6,9.0]
from collections import defaultdict
d = defaultdict(list)
for x in list:
    d[type(x)].append(x)

print( d[int])
print(d[str])
print(d[float])
#Q.5- Using range(1,101), make a list containing only prime numbers.
for num in range(1,101):
    if all(num%i!=0 for i in range(2,num)):
        print(num)
#Q.6- Print the following patterns: 
#* 
#** 
#*** 
#****

def printSeriesIncreasing1(symbol,n):
    count=1
    while count<=n:
        print(symbol*count)
        count=count+1
    return

printSeriesIncreasing1('*',5)

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
ac=list(map(int.input("enter the elements").split()))
element=int(input("enter the element to search"))
if element in ac:
    print("element found")
    del.1[ac.index(element)]
    print(ac)
