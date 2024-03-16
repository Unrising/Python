# scope = the region that a variable is recognized

# A variable is only available from inside the region it is created

# A global and locally scoped versions of a variable can be created

# first => Local 
# Second => Enclosing
# Third => Global 
# Fourth => Built-in 


name = "Bro" # global scope

def display_name():
    name = "Code" # local scope
    print(name)

display_name()

print(name)


