#w5d1 1d list review plus function review plus seq. search

import csv


#create empty list
lname = []
fname = []
test1= []
test2 =[]
test3 =[]

# to be created 
num_avg = []
let_avg = []

#Functions -----------------------------

def menu():

    print("-CLASS ACCOUNT MENU-")
    print("1. Show all students")
    print("2. Show roser only")
    print("3. Search for a student")
    print("4. EXIT")

    choice = input("Enter your choice [1 - 4]: ")

    # loop trap my user if they dont follow the directions 
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("*INVALID ENTRY* DIGITS 1 - 4 ONLY")
        choice = int(input("Enter your choice [1 - 4]:"))
        

    return choice


def seq_search(search_term):
    #search_term is a local var name and only exists in this definition block 

    found_index = ""


    # sequential search - "in sequence" -> start @ beginning (0) go to the end (len(listname))
    for i in range (0, len(fname)):

        if lname[i] == search_term:
            found_index = i

#file connection/list population------------
with open("week5/listPractice1.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append file data to appropriate lists
        lname.append(rec[0])
        fname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnected from file
print(f"{'LAST':12} \t {'FIRST':12} \t {' T1':4} \t {' T2':4} \t {' T3':4}")
print('------------------------------------------------------')

#populate additional lists - num_avg and let_avg
for i in range(0, len(fname)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(avg)
    
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    elif avg < 60:
        letter = "F"
    else:
        letter = "ERROR @ I:" + str(i)
    
    let_avg.append(letter)

#test file by printing
for i in range(0,len(lname)):
    print(f"{lname[i]:12} \t {fname[i]:12} \t {test1[i]:4} \t {test2[i]:4} \t {test3[i]:4} \t {num_avg[i]:5.1f} \t {let_avg[i]:3}")
#main code-----------------------


#allow a user to choose an option from a menu and display certain data 
#user will repeatedly see the menu until they choose to exit

#show user menu, store choice into a var, use the var for the loop

menu_choice = menu()

while menu_choice != 4: #4 means exit

    #determine what user wants to do
    if menu_choice == 1:
        print("Showing all file data")
    elif menu_choice == 2:
        print("\n\t--Showing class roster--")
    else: #menu choice 3
        print("\n\t--Search for a student--")

        search = input("enter the last name you are looking for: ")

        found = seq_search(search)

        if found != "":

        else:
            print(F"The Student {search} could not be found")
    
    menu_choice = menu()

print("\n\n\tThanks for using the program. Goodbye!")

input("\n\n\nenter to continue.....")