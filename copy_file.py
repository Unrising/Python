# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("D:\\text.txt", "D:\\test.txt")  #src,dst

shutil.copy("D:\\text.txt", "D:\\test.txt") #src,dst

shutil.copy2("D:\\text.txt", "D:\\test.txt") #src,dst

