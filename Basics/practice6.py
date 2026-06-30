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
    if(n==0): #base case - the condition under which the recursion stops, it is used to prevent infinite recursion and stack overflow errors.
        return
    print(n)
    show(n-1)

show(5)
show(20)

#stack overflow error - an error that occurs when the call stack pointer exceeds the stack bound, it is caused by infinite recursion or too many nested function calls. It can be prevented by using base cases in recursive functions and limiting the depth of recursion.
#stack - a data structure that follows the Last In First Out (LIFO) principle, it is used to store function calls and local variables in a program. It is used to keep track of the execution of a program and to manage memory allocation and deallocation.
#stack pointer - a pointer that points to the top of the stack, it is used to keep track of the current position in the stack and to manage memory allocation and deallocation. It is used to prevent stack overflow errors and to manage the execution of a program.

n = 5
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(10)


def cal_nn_sum(n):
    if(n==0):
        return 0
    return cal_nn_sum(n-1) + n  

print(cal_nn_sum(5))


def print_list(list,idx):
    print(list[idx])
    if(idx==len(list)-1):
        return
    print_list(list,idx+1)
list = ["hyderabad","bangalore","chennai","delhi"]
print_list(list,0)
print_list(list,1)
