# while loop = a statement that will execute as long as it's condition remains true

#Infinite loop

# while 1==1: 
#   print("Help !")

#Example 1
name = ""

while len(name) == 0:
    name = input("enter your name !:")

print("Hello " + name)

#Example 2 
name = None 

while not name: 
        name = input("enter your name !:")

print("Hello " + name)
