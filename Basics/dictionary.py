#dictionary 
#dictionary is a collection of key-value pairs
#dictionary is mutable, meaning we can change the values of the dictionary
#dictionary is defined by using curly braces {}
#dictionary is unordered, meaning we cannot access the values of the dictionary by index
dict = {"name":"Gamana","age":20,"college":"college"}

dict2 = {
    "name" : "Prathyusha",
    "age" : 25,
    "college" : "college"
}
dict["namee"] = "Pathu"
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["college"])
print(type(dict))
print(len(dict))

#methods of dictionary
print(list(dict.keys()))
print(dict.keys())#return all keys of the dictionary
print(dict.values())# return all values of the dictionary
print(dict.items()) #retuns all key value pairs of the dictionary
print(dict.get("name"))
print(dict.get("age"))
print(dict.get("college"))
print(dict.get("name","Not found")) #Gamana
print(dict.get("age","Not found")) #20
print(dict.get("college","Not found")) #apna college

#all data types are allowed in dictionary
dict3 = {
    "name" : "Gamana",
    "age" : 20,
    "college" : "Apna college",
    "marks" : [90,80,70,60,50],
    "address" : {"city":"Hyderabad","state":"Telangana"},
    "is_student" : True
}

null_dic = {}
null_dic["name"] = "Gamana"
null_dic["age"] = 20
print(null_dic)


student = {
    "name" : "Gaya",
    "sub" : {
        "ph" : 90,
        "ch" : 80,
    }
}

print(student)
print(student["sub"]["ph"])

stu =  {"city":"Hyderabad","name":"Gamana"}
student.update(stu)
print(student)