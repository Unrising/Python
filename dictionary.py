# dictionary = A changeable , unordered collection of unique key:value pairs 
# Fast beacause they uses hashing , allow us to access a value quickly


capitals = {'USA':'Washington DC',
            'INDIA':'New Delhi',
            'CHINA':'Benjing',
            'RUSSIA':'Moscow'}


capitals.update({'Germany':'Berlin'}) # Adds germany
 
capitals.update({'USA':'Las Vegas'}) # Change washington dc to las vegas

capitals.pop('RUSSIA') # Remove RUSSIA

# capitals.clear() # clear the dictionary

print(capitals['CHINA'])

# print(capitals['Germany']) # We get an error
print(capitals.get('Germany')) # Prints none

print(capitals.keys()) # Prints out the keys
print(capitals.values()) # Prints out the values
print(capitals.items()) # Prints everything

for key,value in capitals.items():
    print(key,value)
