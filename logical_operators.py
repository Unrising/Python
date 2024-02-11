# logical operators (and,or,not) check two or more conditional statement

temp = int(input("What is the temperature ? :"))

if not(temp >= 0 and temp <= 30): # not makes true to false and viceversa
    print("The temperature is good")

elif temp < 0 or temp > 30 : # its true if one the statement is true 
    print("The temperature is bad")
