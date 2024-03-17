import os 

source = "D:\\text.txt"
destination ="D:\\Nouveau dossier\\text.txt"


try:
    if os.path.exists(destination):
        print("There is already a file there named " + source )
    else: 
        os.replace(source,destination)
        print(source + " was moved")

except FileNotFoundError as e:
    print(e)
    print(source + " was not found")


