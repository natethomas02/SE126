import csv 

fname = []
lname = []
age = []
nick_name = []
house_alleg = []
motto_assign = {
        'House Stark': "Winter is Coming",
        'House Baratheon': "Ours is the fury.",
        'House Tully': "Family. Duty. Honor.",
        "Night's Watch": "And now my watch begins.",
        'House Lannister': "Hear me roar!",
        'House Targaryen': "Fire & Blood"
    }


with open ("lab4_ind/lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(rec[2])
        nick_name.append(rec[3])
        house_alleg.append(rec[4])

print(f"{'FIRST':10} \t {'LAST':7} \t {'AGE':2} \t {'NICKNAME':10} \t {'HOUSE ALLEGIANCE':10}")
print("---------------------------------------------")

for i in range(0, len(fname)):

    print(f"{fname[i]:10} \t {lname[i]:7} \t {age[i]:2} \t {nick_name[i]:10} \t {house_alleg[i]:10}")



