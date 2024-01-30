#Nathan Thomas
#SE126.10
#1.26.24
#program prompt-Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.
#
#variable dictionary-
#
#desktop_cost = 2000
#laptop_cost = 1500
#total_records = 0
#total_cost = new_desktop_cost + new_laptop_cost
#desktop_count = 0
#laptop_count = 0
#


#MAIN CODE---------------------------------------------------------------

#import csv
import csv
#assign cost CIO wants to spend
desktop_cost = 2000
laptop_cost = 1500

#records counter for all records
total_records = 0


#create list
comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []

#HEADER------------------------------------
print(f"\n{'TYPE':8} {'MANU':7} {'PROC':2} {'RAM':3} {'HDD1':2} {'#HDD':3} {'HDD2':6} {'OS':3} {'YEAR':6}")


with open ("lab3/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        #track the rec count in file
        total_records += 1

        #comp type---------rec[0]        
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "*ERROR --" + str(rec[0])
        
        #manufacture -------------- rec[1]
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


        
        #append values to list
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



#process list : print machine data
for index in range (0, total_records):

    print(f"{comp_type_list[index]:8} {manu_list[index]:8} {processor_list[index]:3} {ram_list[index]:3} {hdd_1_list[index]:5} {num_hdd_list[index]:3} {hdd_2_list[index]:6} {os_list[index]:4} {year_list[index]:4}")
#process the list to count laptop count and desktop count, and calculate if they are manufactured in the year or before the year 2016
desktop_count= 0 
laptop_count = 0
for index in range(0, len(comp_type_list)):
 if comp_type_list[index] == "Desktop" and int(year_list[index]) <= 16:
        desktop_count += 1
        new_desktop_cost = desktop_count * desktop_cost
 elif comp_type_list[index] == "Laptop" and int(year_list[index]) <=16:
     laptop_count += 1 
     new_laptop_cost = laptop_count * laptop_cost
# calculate total cost of machines that need to be replaced
total_cost = new_desktop_cost + new_laptop_cost


print("\n--------------------------------------")
#print end of records header
print("- End of record report. -")
print("----------------------------------------")
#print out, total desk top and laptops that need to be replaced along with the prices to replace 
print("Based on the report: :")
print(f"\nThere were a total of {desktop_count} desktops found that needed to be replaced.")
print(f"\tTo replace {desktop_count} Desktops it will cost: ${new_desktop_cost:.2f} ")
print(f"\nThere were a total of {laptop_count} laptops found that needed to be replaced.")
print(f"\tTo replace {laptop_count} Laptops it will cost: ${new_laptop_cost:.2f} ")
print("\n-----------------------------------------------------------------------------------")
#print the total combined price of desktop and laptops that need to be replaced 
print(f"The total cost of the company to replace both desktops and laptops is: ${total_cost:.2f}")
print("------------------------------------------------------------------------------------")
#print goodbye message
print("\nGoodbye!")