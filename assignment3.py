#Q.1- Create a list with user defined inputs.
lst = list(input().split())
print(lst)
#Q.2- Add the following list to above created list: 
lst = lst + ['google','apple','facebook','microsoft','tesla'] 
print(lst)
#Q.3 - Count the number of time an object occurs in a list.
print(lst.count('google'))
#Q.4 - create a list with numbers and sort it in ascending order.
lst1 = [11,35,22,67,58,9]
lst1.sort()
print(lst1)
#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
A = [2,4,6,8,10]
B = [1,3,5,7,9]
C = A+B
C = sorted(C)
print(C)
#Q.6 - Count even and odd numbers in that list.
lst2 = [2,3,4,6,7]
no_even = 0
no_odd = 0
for i in lst2:
    if i%2==0:
        no_even += 1
    else:
        no_odd += 1
print("count of even numbers:"+str(no_even))
print("count of odd numbers:"+str(no_odd))

#Tuple
#Q.1-Print a tuple in reverse order.
tup = [4,5,6,7,8]
print(tup[::-1])
#Q.2-Find largest and smallest elements of a tuples. 
tup = [3,4,5,6,7]
print("Largest:",max(tup),"smallest:",min(tup))

#String
#Q.1- Convert a string to uppercase.
str1 = "Hello World"
str1 = str1.upper()
print(str1)
#Q.2- Print true if the string contains all numeric characters.
str2 = "123456"
#Q.3- Replace the word "World" with your name in the string "Hello World".
str3 = "Hello World"
str3 = str3.replace("World","Kittu")
print(str3)

