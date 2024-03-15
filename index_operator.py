# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "michael Picard!"

# if(name[0].islower()):
#     name = name.capitalize()

# print(name)

first_name = name[0:7].upper()
# first_name = name[:7].upper() # works the same

# last_name = name[8:15].lower() # works the same
last_name = name[8:].lower()

last_char = name[-1]

print(first_name,last_name,last_char)