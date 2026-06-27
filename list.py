#list
#list is a collection of items in a particular order
#list is mutable, meaning we can change the values of the list
#list is defined by using square brackets []
marks = [90,80,70,60,50,40,30,20,10]
print(marks)
print(marks[0])
print(marks[5])
print(type(marks))
print(len(marks))

#list can contain items of different data types
list1 = [1,2,3,4,5,"Gamana",90.5,True]
print(list1)
print(list1[3])

#strings are immutable in python , list are mutable in python
list1[3] = 100
print(list1)
print(marks[:4])
print(marks[4:])
print(marks[::2])
print(marks[::3])
print(marks[-3:])
print(marks[:-3])
print(marks[-3:-1])

#list methods

arr = [23,56,12,32]
print(arr)
arr.append(33)
print(arr)
arr.sort()
print(arr)
arr.reverse()
print(arr)
arr.insert(2,100)
print(arr)
arr.sort(reverse=True) #descending order
print(arr)

list = ['z','a','b','c','d']
list.sort(reverse=True)
print(list)
list.reverse()
print(list)

mar = [2,3,4]
mar.insert(1,1)
print(mar)
mar.pop(0)
print(mar)


