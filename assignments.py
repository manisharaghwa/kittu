#code tto sort a dictionary by value
d1={"kriti": 45,"kajal": 34, "riya":23}
print(d1)
print(sorted(d1))
print(sorted(d1.values()))
print('-'*20)

#code to add a key in dictionary
d1={0:1,1:20}
print(d1)
d1[2]=30
print(d1)
print('-'*20)

#code to concatenate dictionaries
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print("concatenated dictionary is:")
print(dict1)
print('-'*20)


#code to iterate over dictionaries using for loops
subjects={'networking':'oops','complier':'expression','maths':'logics'}
for name_key, value in subjects.items():
    print(name_key, 'corresponds to',subjects[name_key])
print('-'*20)

#code to generate and print a dictionary that contains a number (betwwen 1&n)
#in the form of(x,x*x)
n=int(input('enter a number:'))
d=dict()
for x in range(1,n+2):
    d[x]=x*x
print(d)
print('-'*20)

#code to print a dictionary where the keys are numbers b/w 1615 and values
#square of keys
d=dict()
for x in range(1,15):
    d[x]=x**2
print(d)
print('-'*20)

#code to merge two dictionaries.
dict1={'A':10,'B':20}
dict1={'C':30,'D':40}
dict1.update(dict2)
print("merged dictionary is:")
print(dict1)
print('-'*20)

#code to sum all the items in a dictionary
d1={'python':21,'perl':45,'ruby':75}
print("sum of all the values is:")
print(sum(d1.values()))

#code to check a given key already exists in dictionary
animals={'dog':12,'cat':10,'lion':13}
def key(z):
    if z in animals:
        print("key is present:")
    else:
        print("key is not present:")
print('-'*20)


