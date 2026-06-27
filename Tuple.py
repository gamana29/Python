#Tuple 
#Built-in data structure in python
#Tuple is a collection of items in a particular order
#A built-in data type that lets us create immutablesequence of values
#Tuple is defined by using parentheses ()
#just like string they are immutable, meaning we cannot change the values of the tuple


tuple = (1,2,3,4,5,6,7,8,9)
print(type(tuple))
print(tuple)
print(tuple[0])
print(tuple[5])
#tuple[0] = 10 #this will give an error because tuple is immutable

tup = (1,)
print(type(tup))
print(tup)
tup2 = (1)
print(tup2)

print(tuple[1:3])


#Methods of tuple
tup3 = (1,2,3,4,5,1,7,1,2,1)
print(tup3.count(1)) #count total occurance
print(tup3.index(7)) #returns index of first occurance


#practice

movies = []
m1 = str(input("enter movie name:"))
m2 = str(input("enter movie name:"))
m3 = str(input("enter movie name:"))
movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)

fmov = []
fmov.append(input("enter 1:"))
fmov.append(input("enter mov2:"))
fmov.append(input("enter mov3:"))
print(fmov)

listt = [1,2,3,2,1]
num = listt.copy()
num.reverse()
print(num)

if(num==listt):
    print("palindrome")
else:
    print("not palindrome")


tupp = ("C","D","A","A","B","B","A")
print(tupp.count("A"))

li = ["C","D","A","A","B","B","A"]
li.sort()
print(li)
li.remove("A")
print(li)
li.append("F")
print(li)
