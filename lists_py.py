# list = used to store multiple items in a single variable


foods = ["pizza","Coke","Hamburger","Coconut"]

print(foods[0])

foods[0] = "sushi"

print(foods[0])

for food in foods: 
    print(food)
    
# usefull function 
    
foods.append("ice cream") #add at the end 

foods.remove("Coke")

foods.pop() #remove last

foods.insert(3,"Cake") # insert at the third place 

foods.sort() # sort the list by letter

foods.clear() # clear the list 
 
for food in foods: 
    print(food)
