#nathan thomas
#se126.10
#2.3.2024
#program prompt -Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.  After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student. Process through this 2D list to display the data from the file (it should appear just like your previous 3 prints!)
#
#
#
#variable dictionary- 
# avg = 0
# total_count = 0 
# low_avg = 100
#
#
#--------------------------------------------------------
import csv 

#create 1d lists [will be parallel to each other]
#base lists on fields in file

fname = []
lname = []
test1 = []
test2 = []
test3 = []

# connect to file and read data into 1d lists 

with open("week4/files/listPractice1-1.txt") as csvfile:

    file = csv.reader(csvfile)

    # come back and show print(file) later
    for rec in file:
        #store data from file fields to their respective lists
        #by parallel - storing initial file record data at same postition (index) in each list --> use the same [index] across each list to find "matching" data
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))  #cast as int for math
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
# disconnect from file ---------------------------------------------------------

#process the list --> for loop
print(f"{'First':10} \t {'Last':7} \t {'Test 1'} \t {'Test 2'} \t {'Test 3'}")

print("----------------------------------------------------")

for i in range(0, len(fname)): #len() --> returns length of item -> for lists, it is the # of items in the list 

    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")

print("----------------------------------------------------")

#calculate and store each students average test score

avg = 0
total_count = 0 
average = [] 
letter_average = []

for i in range(0, len(test1)):

    #calculate average for student
    avg = (test1[i] + test2[i] + test3[i]) / 3
    
    #append this avg to the average[]

    average.append(avg)

    #assign letter grade
    if avg >= 90:
        letter_average.append('A')
    elif 80 <= avg < 90:
        letter_average.append('B')
    elif 70 <= avg < 80:
        letter_average.append('C')
    elif 60 <= avg < 70:
        letter_average.append('D')   
    else:
        letter_average.append('F') 

# display students fname and test average 
print(f"\n{'FIRST':16}\t{'AVERAGE'}\t{'LETTER GRADE'}")
print("---------------------------------------------")
for i in range(0, len(fname)):
    print(f"{fname[i]:15} \t {average[i]:8.1f} \t {letter_average[i]}")

# Sequential search - "in sequence" --> from beginning through the end
low_name = ""
low_avg = 100 #start with highest value to drop to find lowest 

for i in range(0, len(average)):

    #determine if current average is lower than current low_avg
    if average[i] < low_avg:
        
        low_avg = average[i] # current average is lower, so becomes new low value
        
        low_name = fname[i]


    # display : total students in file
print(f"STUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")

#-------2D Lists-----------------
#use your 1D parallel lists to populate a new, 2d list
#HINT the 2d list is a list ..... populated with lists 
all_students = [] 

for i in range(0, len(fname)):
    num_avg = average[i]
    letter_avg = letter_average[i]
    #add each students data to their (index) place in the all_students[]
    all_students.append([fname[i],lname[i],test1[i],test2[i],test3[i],average[i], ])


print(f"\n-------2D LISTS- individual values----")
#display the 2D list to the console - for now , just get the lists to display ie ['floyd', 'eastham', '100','85','93']

for i in range(0, len(all_students)):
    print(f"{all_students[i]}")

    #display the 2d list to the console where each value for each list appears as a value (and not a list item)
for i in range(0, len(all_students)):
    #we have lists within a list - outter for handles main list (all_students)
    for x in range(0, len(all_students[i])):
        # inner for handles each value found at current list (all_students[i])
        print(f"{all_students[i][x]}", end="\t")

    #include an extra empty print() to cancel the interior prints end =""
    print()