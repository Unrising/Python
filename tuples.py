# tuple = collection wich is ordered and unchangeable used to group related data


student = ("Michael","24","M")

print(student.count("Michael"))

print(student.index("M"))


for information in student :
    print(information)

if "Michael" in student:
    print("Michael is here")