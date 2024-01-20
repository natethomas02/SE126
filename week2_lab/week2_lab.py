import csv
total_records = 0
records_processed = 0


room = []
maxpeople = []
regpeople = []



with open("week2_lab/lab2a.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
    
        print(rec)


        room.append(rec[0])
        maxpeople.append(int(rec[1]))
        regpeople.append(int(rec[2]))

        