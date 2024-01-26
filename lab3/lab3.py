import csv
desktop_cost = 3000
laptop_cost = 1500
total_records = 0
new_desktop = 0
new_laptop = 0

comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []


print(f"\n{'TYPE':8} {'MANU':7} {'PROC':2} {'RAM':3} {'HDD1':2} {'#HDD':3} {'HDD2':6} {'OS':3} {'YEAR':6}")


with open ("lab3/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 


        total_records += 1


        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "*ERROR --" + str(rec[0])

        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR --" + str(rec[1])

        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        if rec[5] == "1":
            hdd_2 = " " #"---" #"none"
            os = rec[6]
            year = rec[7]
        
        
        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
        
        else:
            hdd_2 = "*ERROR --" + str(rec[5])
            os = "ERROR"
            year = "ERROR"

        if str(year) <= int(16):
            new_desktop +=1

        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        hdd_2_list.append(hdd_2)
        num_hdd_list.append(num_hdd)
        os_list.append(os)
        year_list.append(year)




print("--------------------------------------------------")

for index in range (0, total_records):

    print(f"{comp_type_list[index]:8} {manu_list[index]:8} {processor_list[index]:3} {ram_list[index]:3} {hdd_1_list[index]:5} {num_hdd_list[index]:3} {hdd_2_list[index]:6} {os_list[index]:4} {year_list[index]:4}")






print(f"To replace {new_desktop}Desktops it will cost: $ ")
print(f"To replace Laptops it will cost: $ ")