# Name- Late Thomas
# Date - 2.13.2024
# Class - SE126.10
# Program prompt- For this midterm project I wanted to continue on from last semesters mid term. The program I decided to build pulls the list of lifters that were entered in for a lifting event. The program contains a menu that lets you choose from, Viewing everone that was entered into the event, showing the light-weight class/ the program calculates from the list who falls into the 'light-weight class' based off their body weight, shows everyone in the 'heavy-weight class' also calculated by body weight, anyone less than 185LBS falls into the light weight and anyone over is in the heavy weight class. After they are split into classes it counts for both classes the number of individuals that fall into that class and then lists their names, age, body weight, then bench press pr, squat pr, and deadlift pr, after it processes all 3 it calculates the sum of all 3 lifts and computes a total of all 3. The menu also lets you choose to search for one individual, showing the same exact stats if you intend to just focus on one person.


import csv

fname = []
age = []
weight = []
bench = []
squat = []
deadlift = []

lift_sum = []
light_weight_group = []
heavy_weight_group = []

def club_status(total_lift):
    if total_lift >= 1000:
        return "This lifter is in the 1000lb club!"
    else:
        return "This lifter is not in the 1000lb club."

def menu():
    print(" \n- ANNUAL POWER HOUSE LIGHT-WIGHT & HEAVY-WEIGHT EVENT -")
    print("1. Show all named entries.")
    print("2. Show all Light-weight scores.")
    print("3. Show all heavy-weight scores.")
    print("4. Search for an entry.")
    print("5. EXIT")

    choice = input("Enter your choice [1 - 5]: ")

    return choice

def seq_search(search_term):
    found_index = -1  # Initialize to -1 if not found
    for i in range(len(fname)):
        if fname[i] == search_term:
            found_index = i
            return found_index
    return found_index

with open("midterm/lifting.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        fname.append(rec[0])
        age.append(int(rec[1]))
        weight.append(int(rec[2]))
        bench.append(int(rec[3]))
        squat.append(int(rec[4]))
        deadlift.append(int(rec[5]))


for i in range(0, len(fname)):
    total_lift = bench[i] + squat[i] + deadlift[i]
    lift_sum.append(total_lift)
    if weight[i] < 185:
        light_weight_group.append((fname[i], age[i], weight[i], bench[i], squat[i], deadlift[i], total_lift, club_status(total_lift)))
    else:
        heavy_weight_group.append((fname[i], age[i], weight[i], bench[i], squat[i], deadlift[i], total_lift, club_status(total_lift)))

    

    

menu_choice = menu()

while menu_choice != '5':
    if menu_choice == '1':
        
        print("-----------------------------")
        print("Showing all named entries.")
        count = len(fname)
        print(f"Total number of named entries: {count}")
        print("-----------------------------")
        print("NAME \t AGE \t WEIGHT")
        print("-----------------------------")
        for i in range(0, len(fname)):
            print(f"{fname[i]:9} {age[i]:1} {weight[i]:8}")
            print("-----------------------------")

    elif menu_choice == '2':
       

        print("\n\t Showing All Light-Weight Scores.")
        count = len(light_weight_group)
        print(f"\tNumber of entries in light-weight group: {count}")
        print(f"\n{'NAME':10} {'AGE':6} {'WEIGHT':8} {'BENCH':8} {'SQUAT':7} {'DEADLIFT':10} {'TOTAL-LIFT':9} {'CLUB-STATUS':15}")
        print("---------------------------------------------------------------------")
        
        for i in range(len(light_weight_group)):
            entry = light_weight_group[i]
            print(f"{entry[0]:7} {entry[1]:5} {entry[2]:7} lbs {entry[3]:4} lbs {entry[4]:4} lbs {entry[5]:5} lbs {entry[6]:7} lbs {entry[7]}")
            print("---------------------------------------------------------------------")

    
    elif menu_choice == '3':
        print("\n\t Showing All Heavy-Weight Scores.")
        count = len(heavy_weight_group)
        print(f"\tNumber of entries in heavy-weight group: {count}")
        print(f"\n{'NAME':10} {'AGE':6} {'WEIGHT':9} {'BENCH':8} {'SQUAT':7} {'DEADLIFT':10} {'TOTAL-LIFT':9}")
        print("---------------------------------------------------------------------")
        
        for i in range(len(heavy_weight_group)):
            entry = heavy_weight_group[i]
            print(f"{entry[0]:7} {entry[1]:5} {entry[2]:7} lbs  {entry[3]:4} lbs {entry[4]:4} lbs {entry[5]:5} lbs {entry[6]:7} lbs")
            print("---------------------------------------------------------------------")

    elif menu_choice == '4':
        print("\n\t--Search for an entry--")
        search = input("\n\tEnter the first name you are looking for: ")
        found = seq_search(search)
        if found != -1:
            print(f"\tFound entry for {search}:")
            print(f"\nName: {fname[found]}, Age: {age[found]}, Weight: {weight[found]} lbs, Bench: {bench[found]} lbs, Squat: {squat[found]} lbs, Deadlift: {deadlift[found]} lbs")
        else:
            print(f"The entry for {search} could not be found.")

    menu_choice = menu()
