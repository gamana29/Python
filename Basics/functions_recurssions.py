#functions 

def add(a,b):
    return a+b  
print(add(2,3))


def sn(a,b):
    sum = a+b
    return sum
print(sn(5,23))
print(sn(2,2))
print(sn(5,23))
print(sn(2,2))
print(sn(5,23))
print(sn(2,2))


def cal_sum(a,b):
    return a-b
print(cal_sum(100,90))

#func(arg1,arg2,arg3) #function call


def cal(a,b):
    return a*b
print(cal(2,3))


#function definition
def cal(a,b): #parameters
    return a/b
sum = cal(10,2) #function call #10,2 are arguments
print(sum)

def print_hELLO():
    print("Hello")
print_hELLO() #function call
print_hELLO() #function call
print_hELLO() #function call
print_hELLO() #function call

print(print_hELLO()) #function call #None is printed because the function does not return anything, it only prints "Hello"



#average of 3 numbers
def avg(a,b,c):
    sum = a+b+c
    a = sum/3
    return a
    print(a)
avg(10,20,30) #function call


print("gamana")


print("gamana", end = " ") #sep = " " is used to separate the values with a space
print("chirumamilla") #end = "\n" is used to print the next value in a new line


#builtin functions

#user defined functions

#defaultparameters
def cal(a,b=2): #b is a default parameter
    return a*b
print(cal(5)) #function call #b is not passed, so it takes the default value of 2

