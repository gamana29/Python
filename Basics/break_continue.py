# #break - code gets terminated when the condition is met
# i=1
# while i<=10:
#     if  i == 3:
#         break
#     print(i)
#     i+=1


# #continue - code gets skipped when the condition is met
# i=1
# while i<=5:
#     if i == 3:
#         i+=1
#         continue #skips the current iteration and moves to the next iteration
#     print(i)
#     i+=1


i = 0
while i<=10:
    if (i%2==0):
        i+=1
        continue
    print(i)
    i+=1