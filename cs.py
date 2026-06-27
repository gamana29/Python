#conditional statements

age = int(input("enter your age:"))
if (age==18):
    print("you are eligible to vote, register")
elif (age>=18):
    print("you are  eligible to vote") #indentation
else:
    print("you are not eligible to vote")


marks = int(input("enter marks: "))

if (marks>=90):
    print("A grade")
elif (marks>=80 | marks<90):
    print("B grade")
elif(marks>=70 | marks<80):
    print("C grade")
else:
    print("D grade")