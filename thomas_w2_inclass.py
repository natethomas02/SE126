import csv
total_records = 0
under_age = 0
elig_notreg = 0
reg_novote = 0
reg_and_voted = 0
age = []
registered = []
voted = []



with open("lab3_homework/voters_202040.csv") as csvfile:

        file = csv.reader(csvfile)

        for rec in file:
                total_records += 1 
                age.append(int(rec[1]))
                registered.append(rec[2])
                voted.append(rec[3])

print(f"Total records processed: {total_records}")



for i in range(total_records):
        if age[i] < 18:
                under_age += 1
        elif age[i] >= 18 and registered[i] == "N":
                elig_notreg += 1
        elif registered[i] == "Y" and voted == "Y":
                reg_novote += 1
        elif registered[i] == "Y" and voted == "Y":
                reg_and_voted += 1

print(f"Individuals not eligible to register: {under_age}")

print(f"Individuals old enough to vote but have not registered: {elig_notreg}")

print(f"Individuals eligible to vote but did not vote: {reg_novote}")

print(f"Individuals voted: {reg_and_voted}")

