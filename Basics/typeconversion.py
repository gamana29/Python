#automatic type convertion in python

#type conversion

a = 2
b = 4.25
sum = a+b
print(sum)

#type conversion - automatic type conversion
#float is higher than int, so int is converted to float and then addition is performed

c = "2"
d = 3.2
e = int(c)
sum2 = e+d
print(sum2)

f = int("2")
g = float("3.2")
print(f+g)

#type conversion - explicit type conversion
#type casting - converting one data type to another data type
#type casting is done by using the constructor functions of the data types
#type casting is done only when the data types are compatible