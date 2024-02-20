#w7d1 comparing searching methods demo

# this demo covers : sequential search (review) , Binary search (intro) bubble sort(intro)

#Librarires-----------------
import csv


#Functions -----------------


#Main program --------------------


# create empty 1d lists to hold data in text file 

id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("w7_demo/w7_demoFile.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

    
        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#check fule connectivity
for i in range (0, len(id_stud)):
    print(f'{id_stud[i]}\t{lname[i]}\t{fname[i]}')

#sequential search -- searching in sequence (from beginning, through the end)

search_name = input("Enter the name you are looking for: ")
#found = -1
found = []# allows for multiples in search


#for loop allows review of each value in list (sequence)
for i in range(0, len(fname)):

    #ask if search value matches current value in list
    if search_name.lower() == fname[i].lower():

        #store found values location (index) 
        found.append[i]
    
if found[0] != "":
    print(f"We found {search_name} at index position: {found}")
    print("\tHere is their info: ")

    for i in range(0 , len(found)):

        print(f"\t\t{fname[found[i]]} \t{lname[found[i]]} \t {id_stud[found[i]]} \t {class1[found[i]]} \t {class2[found[i]]} \t {class3[found[i]]}\n")
else:
    print(f"\n\tWe could not find {search_name} :[ ")
    print("\tPlease try again.\n")



# binary search --- take an ordered list and divide into 2 sections (hugh, low) and based on a middle point will continually halve the search pool until a uniqe value is found (or one isnt)

search_name = input("enter the LAST NAME you are looking for: ")

min = lname[0] # first position of the list to be searched 
max = lname[len(lname) - 1] #last position of the list to be searched (ascending)
#mid = int((0 + (len(lname) - 1)) / 2) 

mid = int((min + max) / 2)
bin_count = 0
#this is for increasing (ascending) order

while (min < max and search_name != lname[mid]):
    bin_count += 1

    if search_name < lname[mid]:
        max = mid - 1 
    else: 
        min = mid + 1 

    mid = int((min + maX) / 2)

if search_name == lname[mid]:

    #found them! use 'guess' for index of found search item
    print(f"\t\t{fname[mid]} \t{lname[mid]} \t {id_stud[mid]} \t {class1[mid]} \t {class2[mid]} \t {class3[mid]}\n")

else: 
#not found
    print(f"We could not find {search_name}")
    print()


#BUBBLE SORT----------------------------------------

nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]


print(f"Current List: {nums}")




for i in range(0, number_of_elements - 1):#outter loop

    print("OUTER LOOP! i = ", i)


    for index in range(0, len(nums) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort

        #list used is the list being sorted

        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):

            print(f"\t\t SWAP! {nums[index]} <--> {nums[index + 1]}")

            #if above is true, swap places!

            temp = nums[index]

            nums[index] = nums[index + 1]

            nums[index + 1] = temp

 
            #swap all other values

            temp = nums[index]

            nums[index] = nums[index + 1]

            nums[index + 1] = temp

print(f"Sorted list : {nums}")

