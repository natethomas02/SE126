# required documentation 
#
# Nathan Thomas
# 1/20/24
# SE126
# Program prompt - he csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event. Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.
#records_processed = 0
#rooms_over_limit = 0
#
#
#
#-------MAIN CODE------------------------------------------------------------------------------------

#define the process for the rooms, set to 0 for counters
def process_rooms(filename):
    records_processed = 0
    rooms_over_limit = 0

    #open csv/txt file as a parameter 
    with open(filename, 'r') as file:
        # print header for columns
        
        print("{:<20} {:<15} {:<15} {:<10}".format('Room', 'Max', 'Reg.', 'Over'))
        #for loop start, include records counter
        for line in file:
            records_processed += 1

            # Split the line into fields
            room_name, max_cap, current_registered = line.strip().split(',')

            max_cap = int(max_cap)
            current_registered = int(current_registered)
            # if statement to count the rooms over limit , followed by printing the room names, max cap , current registered , and the calculation to figure out how many over the limit
            if current_registered > max_cap:
                rooms_over_limit += 1
                print(f"{room_name :<20} {max_cap : <15} {current_registered : <15} {current_registered - max_cap : <15} ")
#display records processed and rooms over limits
    print(f"\nNumber of records processed: {records_processed}")
    print(f"Number of rooms over limit: {rooms_over_limit}")

# assign lab2a.txt file directory to a variable to use it as a parameter
filename = 'week2_lab/lab2a.txt'

process_rooms(filename)
