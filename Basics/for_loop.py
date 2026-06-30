#for loop

list1 = [1,2,3,4,5]
for i in list1:
    print(i)


veg = ["tamatoo","potato","onion"]
for n in veg:
    print(n)

tuple = (1,2,3,4)
for r in tuple:
    print(r)


s1 = "gamana"
for c in s1:
    if (c =="a"):
        print("found")
        break
    print(c) 
else:
    print("loop is completed")

# else does not work in break condition, it will only work if the loop is completed without any break statement