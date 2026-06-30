for i in range(101):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(1,11):
    print(3*i)


#pass statement

for i in range(5):
    pass #pass statement is used as a placeholder for future code, when the code is not yet implemented, it does nothing and can be used to avoid errors.
print("Hello")


n = 5
s = 0
for i in range(n):
    s+=i
print(s)

n = 7
s=0
i=1
while i<=n:
    s+=i
    i+=1
print(s)

#factorial - for loop
fact = 1
n = 5
for i in range(1,n+1):
    fact*=i
print(fact)

#while loop

fact = 1
n = 6
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)