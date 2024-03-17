
text = "Have a nice day! See ya !"

with open("D:\\text.txt",'a') as file: # 'w' to write (overwrite) 'a' to append text
    file.write(text)
    