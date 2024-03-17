try:
    with open("D:\\text.txt") as file: # Close file auto
        print(file.read())

except FileNotFoundError as e :
    print(e)
    print("The file does not exist")

