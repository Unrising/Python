# nested loops = The "inner loop" will finish when all of it's iterations before 


rows = int(input("How many rown? :"))
colums = int(input("How many columns? :"))
symbol = input("Enter a symbol to use :")

for i in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()

