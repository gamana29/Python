#Sets
#Sets are unordered collection of unique items
#Sets are mutable, meaning we can change the values of the set
#Set is defined by using curly braces {}
#elements should be unique & immutable items in a set

#list and dic cannot be added in set because they are mutable
# tuple can be added in set because they are immutable
#set is mutable but the elements of the set should be immutable

collection = {1,2,3,4,"world",5,6,7,8,9,"world","world"}
# set ignores duplicate values and only keeps unique values
print(collection)
print(type(collection))
print(len(collection))

#repeated values are ignored in set, stored only once

null_set = set() #empty set
print(type(null_set))
print(len(null_set))
print(null_set)

#sets are mutable but the elements of the set should be immutable
#methods of set

null_set.add(1)
null_set.add(2)
null_set.add(3)
null_set.add(1)
null_set.add(2)
null_set.add(3)
null_set.remove(2)
null_set.add("Gamana")
null_set.add((1,2,3)) #tuple are added but not list and dic because they are mutable
print(null_set)
null_set.clear()
print(null_set)
null_set.add(1)
null_set.add(2)
null_set.add(3)
null_set.pop()
print(null_set)
print(null_set.pop())
print(null_set.pop())

sett1 = {1,2,3,4,5}
sett2 = {4,5,6,7,8}
print(sett1.union(sett2)) #all unique elements from both sets
print(sett1)
print(sett2)

print(sett1.intersection(sett2)) #common elements from both sets
print(sett1.difference(sett2)) #elements in sett1 but not in sett
print(sett2.difference(sett1)) #elements in sett2 but not in sett1


#practice 

ddd = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts and fig"]
}

print(ddd)

seett = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(seett))


dic = {}

x = int(input("ent phy:"))
dic.update({"phy" : x})
x = int(input("ent che:"))
dic.update({"che" : x})
x = int(input("ent math:"))
dic.update({"math" : x})

print(dic)

values = {9,'9.0'}
print(values)

val = {("float",9.0),("int",9)}
print(val)
