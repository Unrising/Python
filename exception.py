
try:
    numerator = int(input("Enter a number to divide: "))

    denominator = int(input("Enter a number to divide by: "))

    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You tried to divide by zero")

except Exception as e:
    print(e)
    print("Something went wrong")
    
except ValueError as e:
    print(e)
    print("Enter only number pls")
    
else: 
    print(result)

finally:
    print("Lets Go")