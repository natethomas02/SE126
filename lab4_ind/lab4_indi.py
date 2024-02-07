import csv 

fname = []
lname = []
age = []
nick_name = []
house_alleg = []

with open ("lab4_ind/lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(rec[2])
        nick_name.append(rec[3])
        house_alleg.append(rec[4])