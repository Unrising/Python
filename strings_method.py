# Principals method in python 

name = "Michael"

print(len(name)) # Length of name

print(name.find("M")) # Find M in michael

last_name = "picard"

print(last_name.capitalize()) # Capitalize picard to Picard

print(last_name.lower()) # picard

print(last_name.upper()) # PICARD

print(name.isdigit()) # False because there is no digit

print(name.isalpha()) # True because there are only letters

print(name.count("a")) # 1 because there is only 1 a in Michael

print(name.replace("a","o")) # Michael => Michoel

print(name*3) # prints Michael 3 times