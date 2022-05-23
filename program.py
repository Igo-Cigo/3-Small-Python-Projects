# A program that sorts names in Alphabetical order

import time

names = []

def sort_names():   
    #This function sorts the names in alphabetical order

    names.sort()
    return names

def save_names(names):
    #This function saves the names to a file

    with open('names.txt', 'w') as file:
        for name in names:
            file.write(name + '\n')

lenght = input('How many names do you want to enter? (If unsure leave blank) ')

if lenght == "":
    lenght = 1000000
else:
    lenght = int(lenght)

for i in range(0, lenght):
    name = input(": ")
    names.append(name)

    if name == "":
        e = input("Are you sure you're finished entering names? (y/n) ")
        if e == "y":
            break
        else:
            continue

print("Sorting names...")
time.sleep(0.3)
sort_names()
time.sleep(0.3)
print("Printing names...")
time.sleep(0.3)
print(names)
time.sleep(0.3)
print("Saving names...")
time.sleep(0.3)
save_names(names)
time.sleep(0.3)
print("Done!")
time.sleep(0.3)
quit()