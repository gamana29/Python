list = ["hyderabad","bangalore","chennai","delhi"]
fruits = ["apple","banana","grapes","mango"]    
vegetables = ["carrot","cauliflower"]

def print_len(list):
    print(len(list))

print_len(list)
print_len(fruits)
print_len(vegetables)


def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(vegetables)
print()


def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
print(fact(5))

def ca_f(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
print(ca_f(5))

def factorial(n):
    f=1
    i=1
    while i<=n:
        f*=i
        i+=1
    return f
print(factorial(5))


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fact(5)


#USD to INR
def usd_to_inr(usd):
    inr = usd*84
    return inr
print(usd_to_inr(100))



#recursion - a function that calls itself, it is used to solve problems that can be broken down into smaller sub-problems of the same type. It is a powerful tool for solving problems that can be defined in terms of themselves.

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)
show(20)

