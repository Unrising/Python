# set = collection wich is unordered, unindexed. No duplicates values

untensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife","knife"}

# untensils.add("napkin")
# untensils.remove("fork")
# untensils.update(dishes)

dinner_table = untensils.union(dishes)
# untensils.clear()

print(dishes.difference(untensils)) # check the difference 

print(untensils.intersection(dishes)) # prints the element in common

# for x in untensils: # print in different order
#     print(x)

# for x in dinner_table: # print in different order
#     print(x)

