import csv 

IDs = []
last_names =[]
first_names =[]
class1 = []
class2 = []
class3 = []











def menu():
    print(" \n- ANNUAL POWER HOUSE LIGHT-WIGHT & HEAVY-WEIGHT EVENT -")
    print("1. See all students Report.")
    print("2. Search for student [id].")
    print("3. Search for student [last].")
    print("4. View a class roster [class1, class2, class3].")
    print("5. EXIT")

    choice = input("Enter your choice [1 - 5]: ")

    return 


with open('lab5/lab5_students.txt') as file:
    file = csv.reader(file)
    for rec in file:
        IDs.append(rec[0])
        last_names.append(rec[1])
        first_names.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])


menu_choice = menu()



#print("'IDs' \t 'Last' \t 'First' \t 'class 1' \t 'class 2' \t 'class 3' ")

