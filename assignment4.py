#Q.1- Reverse the whole list using list methods.
lst=[20,30,40,'python','perl','c',14]
lst.reverse()
print(lst)
     
#Q.2- Print all the uppercase letters from a string.
s="My Name is Ashu"
for i in s:
    if i==i.upper():
        print(i,end="|")

#Q.3- Split the user input on comma's and store the values in a list as integers.
lst3=list(map(int,input("Enter a elements").split(",")))
print(lst3)


#Q.4- Check whether a string is palindromic or not.
a=input("Enter a string")
if a[::-1]==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
lst1=[3,4,5]
lst2=lst1
print("original list:",lst1,"id=",id(lst1))
print("shallow copylist:",lst2,"id=",id(lst2))
#deep copy
lst3=lst1.copy()
print("original list:",lst1,"id=",id(lst1))
print("deep copy list:",lst3,"id=",id(lst3))




