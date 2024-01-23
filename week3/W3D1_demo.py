#w3d1 demo - text file handling and storing to 1D lists

import csv 

#total counter for all records 
total_records = 0


#not for hw !!!
#create some lists
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []


#-----HEADER---------------------------
print(f"\n{'TYPE':8} {'MANU':8} {'PROC':6} {'RAM':6} {'HDD1':6} {'#HDD':6} {'HDD2':6} {'OS':6} {'YEAR':6}")
print("------------------------------------------------------")

with open("week3/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)  #shows as a list -> []

        # keep track of the rec count in the file 

        total_records += 1 

        #filter for display------------
        #comp type ---- rec[0]
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "*ERROR -- " + str(rec[0])

        #------Manufacture--------
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            manu = "*ERROR --" + str(rec[1])

        #-----processor / ram / hdd_1 / num_hdd -- exact from file---
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
        
        
        #not for hw !!!
        #append respective values to the appropriate field list
        comp_type_list.append(comp_type)
        manu_list.append(manu)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        hdd_2_list.append(hdd_2)
        num_hdd_list.append(num_hdd)
        os_list.append(os)
        year_list.append(year)

    

        #final print for each record
        print(f"{comp_type:8} {manu:8} {processor:3} {ram:3} {hdd_1:5} {num_hdd:3} {hdd_2:6} {os:4} {year:4}")
#------------------Disconnected from file-------------------
print("------------------------------------------------------\n")

print(f"Total records : {total_records}")


#not for hw !!!
#process the list to : print the machine data
for index in range (0, total_records):
    # for index in range(0, len(comp_type_lsit)): --> len
    #comp_type_list) returns the INTEGER count of values

     print(f"{comp_type_list[index]:8} {manu_list[index]:8} {processor_list[index]:3} {ram_list[index]:3} {hdd_1_list[index]:5} {num_hdd_list[index]:3} {hdd_2_list[index]:6} {os_list[index]:4} {year_list[index]:4}")

     #process th lists to :  count the number of desktops
desktop_count= 0 
for index in range(0, len(comp_type_list)):

        #look through the comp_type_list to find "desktop"
    if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:
        desktop_count += 1 # add 1 for every time "Desktop" is found
print(f"TOTAL DESKTOPS IN FILE: {desktop_count}")

#len() is a length function; when passed a (list) it returns an integer: # of values in list

     #process the lists to : find average hdd_1 size
total_size = 0 
count_size = 0

for index in range(0, len(hdd_1_list)):
    if hdd_1_list[index] == '001TB':
        total_size += 1
    else:
        total_size += 0.5

    count_size += 1
    
average = total_size / count_size #could also use : len(hdd_list_1) or total_records in place of count_size

print(f"AVERAGE HDD#1 SIZE: {average:0.2f}TB or {average*1000:0.2f}GB")



