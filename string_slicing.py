# slicing = create a substring by extracting from another string
# indexing[] or slice()
# [start:stop:step]
 
name = "Michael Picard" # total 15 index

first_name = name[0:7] # or name[:7]
last_name = name[8:15] # or name[8:]

funky_name = name[0:15:2] # or name [::3]

reversed_name = name[::-1] # reversed the string

print(first_name + " " + last_name)

print(funky_name)

print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4,1) # only to get google 

website = website[slice]
website2 = website2[slice]

print(website)
print(website2)