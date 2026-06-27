age = int(input("enter age:"))

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


#practice

num = int(input("enter num:"))

if(num%2==0):
    print("even")
else:
    print("odd")



a = int(input("enter num:"))
b= int(input("enter num:"))
c = int(input("enter num:"))

if(a>b and a>c):
    print("a is greater",a)
elif(b>a and b>c):
    print("b is greater",b)
elif(c>a and c>b):
    print("c is greater",c)
else:
    print("all are equal",a,b,c)


x = int(input("en num:"))

if(x%7==0):
    print("mul of 7")
else:
    print("not mul of 7")
    