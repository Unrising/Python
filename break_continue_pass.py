# Loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing

while True:
    name = input("What is your name ? :")
    if name != "":
        break

code = 1-2-6-4-8-5

for i in code:
    if i == "-":
        continue
    print(i,end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)