#w7d2 - bubble sort and binary search 

import csv 

# create empty 1d lists 

type_ = []
name = [] 
meaning = [] 
origin = []

with open ("w7d2/party.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        type_.append(rec[0])
        name.append(rec[1])         #what we will sort and search by 
        meaning.append(rec[2])
        origin.append(rec[3])

        #sort the file data by first name ascending (increaisng) order
#originial file print
print("original file-----------------------------")
print(f"{'TYPE':8} {'NAME':12} {'MEANING':30} {'ORIGIN'}")

for i in range(0, len(type_)):
    print(f"{type_[i]:8} {name[i]:12} {meaning[i]:30} {origin[i]}")
        #bubble sort---------------------
for i in range(0, len(name)):#outter loop

        


    for index in range(0, len(name)):#inner loop

         

       

        if(name[index] > name[index + 1]):

            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

            #if above is true, swap places!

            temp = name[index]

            name[index] = name[index + 1]

            name[index + 1] = temp

 
            #swap all other values

            temp = type_[index]

            type_[index] = type_[index + 1]

            type_[index + 1] = temp

            #--meaning---
            temp = meaning[index]

            meaning[index] = meaning[index + 1]

            meaning[index + 1] = temp



            #--origin---
            temp = origin[index]

            origin[index] = origin[index + 1]

            origin[index + 1] = temp

        # create a loop for user to repeatedly search through 
        #perform binary search 
        #binary search-------------------

