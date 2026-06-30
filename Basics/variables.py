name = "Gamana" #string 
age = 21
print("My name is", name, "and my age is", age)
print(name,age)
print(name)
print(age)

# each variable is having some memory
print(id(name)) #memory location of variable name

age2 = age
print(id(age2)) #memory location of variable age2
print(id(age)) #memory location of variable age
print("Memory location of age and age2 are same", id(age2) == id(age)) #True
print("Memory location of name and age are same", id(name) == id(age)) #False
print(age)
print(age2)
print("Memory location of name and age2 are same", id(name) == id(age2)) #False

print(type(name)) #string
print(type(age)) #string
print(type(age2)) #string

price = 100.50
print(type(price)) #float
a = 'gamana'
b = "gamanaaa"
c = '''gamanaaaa'''
print(type(a)) #string  
print(type(b)) #string
print(type(c)) #string
print(a)
print(b)
print(c)

#Boolean -- True, False 
# true , false --- wrong


