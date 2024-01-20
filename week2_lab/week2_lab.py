import csv

def process_rooms(filename):
    records_processed = 0
    rooms_over_limit = 0

    with open(filename, 'r') as csvfile:
        file = csv.reader(csvfile)
        
        
        next(file, None)

        for row in file:
            records_processed += 1

            room_name, max_cap, current_registered = row
            max_cap = int(max_cap)
            current_registered = int(current_registered)

            if current_registered > max_cap:
                rooms_over_limit += 1
                print(f"Room {room_name} is over the maximum limit. Notify {current_registered - max_cap} people.")

    print(f"\nNumber of records processed: {records_processed}")
    print(f"Number of rooms over limit: {rooms_over_limit}")


filename = 'week2_lab/lab2a.txt'


process_rooms(filename)
