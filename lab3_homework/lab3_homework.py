#Late Thomas
#se126.10
#1.31.2024
#program prompt-
#variable dictionary-
#total_records = 0
#under_age = 0
#elig_notreg = 0
#reg_novote = 0
#reg_and_voted = 0
#
#
#-------------------------------------------------------------------------
#import csv file
import csv

#Assign variables and lists
total_records = 0
under_age = 0
elig_notreg = 0
reg_novote = 0
reg_and_voted = 0
age = []
registered = []
voted = []

#connect to file and read data
with open("lab3_homework/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #store data from file fields to their lists and total_records counter
        total_records += 1
        age.append(int(rec[1]))
        registered.append(rec[2])
        voted.append(rec[3])
#print total records recorded
print(f"Total records processed: {total_records}")
print("-----------------------------------------------")
#for loop, set counters for appropriate variables
for i in range(total_records):
    if age[i] < 18:
        under_age += 1
    elif age[i] >= 18 and registered[i] == "N":
        elig_notreg += 1
    elif registered[i] == "Y" and voted[i] == "N":
        reg_novote += 1
    elif registered[i] == "Y" and voted[i] == "Y":
        reg_and_voted += 1
#print output
print(f"\nIndividuals not eligible to register: {under_age}")
print(f"\nIndividuals old enough to vote but have not registered: {elig_notreg}")
print(f"\nIndividuals eligible to vote but did not vote: {reg_novote}")
print(f"\nIndividuals voted: {reg_and_voted}")
print("-----------------------------------------------")
# print good bye message
print("\n GOODBYE!")
