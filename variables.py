# variable = a container for a value 
# datatypes : int , string , float , bool , double etc...

###################### STRING ##################################
name = "Michael" # its a string 

print(type("Hello " + name)) # checks the type = str
print("Hello " + name) # print the Hello Michael

first_name = "Michael"
last_name = "Picard"

full_name = first_name + " " + last_name

print(full_name)

###################### INT ####################################

age = 24 # its a int 

print(type(age)) # checks the type = int 
print(age) # print 24
age += 1 
print(age) # print 25

age = str(age) # changed  int age to str age because you can't print int age with a string 

print("Your age is " + age) 

###################### FLOAT ##################################

grade = 10.5 # its a float 

print(type(grade)) # checks the type = float
print(grade) # print 10.5

print("Your grade is " + str(grade)) # You can recast like this 

###################### BOOL ###################################

human = False 

print(type(human)) # checks the type = bool
print(human) # print False

print("Are you human ? : " + str(human)) # You can recast like this