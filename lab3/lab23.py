import csv


machine_ids = []
types = []
years = []
costs = []

with open("lab3/lab3a.csv") as csvfile:
    
    
    for line in csvfile:
        # Split the line into values
        values = line.strip().split(',')
        
        # Store values in separate lists
        machine_ids.append(values[0])
        types.append(values[1])
        years.append(int(values[2]))  # Assuming the year is an integer
        costs.append(float(values[3]))  
        
        
        desktop_replace_count = 0

desktop_replace_cost = 0
laptop_replace_count = 0
laptop_replace_cost = 0

for i in range(len(machine_ids)):
    print(f"Machine ID: {machine_ids[i]}, Type: {types[i]}, Year: {years[i]}, Cost: {costs[i]}")
    
    if years[i] <= 2016:
        if types[i] == "Desktop" and costs[i] <= 2000:
            desktop_replace_count += 1
            desktop_replace_cost += costs[i]
        elif types[i] == "Laptop" and costs[i] <= 1500:
            laptop_replace_count += 1
            laptop_replace_cost += costs[i]

# Print end report
print("\nReplacement Report:")
print(f"Number of Desktops to be replaced: {desktop_replace_count}")
print(f"Cost to replace Desktops: ${desktop_replace_cost}")
print(f"Number of Laptops to be replaced: {laptop_replace_count}")
print(f"Cost to replace Laptops: ${laptop_replace_cost}")
