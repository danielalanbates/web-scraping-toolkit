# Create the initial guest list, overwriting any old file
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
with open("guests.txt", "w") as file:
    for guest in initial_guests:
        file.write(guest + "\n")

# Append new guests to the list
new_guests = ["Sam", "Danielle", "Jacob"]
with open("guests.txt", "a") as file:
    for guest in new_guests:
        file.write(guest + "\n")

# Remove guests that have checked out
checked_out = ["Andrea", "Manuel", "Khalid"]

# Step 1: Read all current guests from the file into a temporary list
temp_list = []
with open("guests.txt", "r") as file:
    for guest in file:
        temp_list.append(guest.strip())

# Step 2: Create a new list containing only the guests who have NOT checked out
guests_to_keep = []
for name in temp_list:
    if name not in checked_out:
        guests_to_keep.append(name)

# Step 3: Overwrite the file with the final, filtered list
with open("guests.txt", "w") as file:
    for guest in guests_to_keep:
        file.write(guest + "\n")

# Print the final guest list to the console
print("Final Guest List:")
with open("guests.txt") as file:
    for line in file:
        print(line.strip())

# Check the status of specific guests from a predefined list
guests_to_check = ['Bob', 'Andrea']
checked_in = []
with open('guests.txt', 'r') as file:
    for guest in file:
        checked_in.append(guest.strip())

print("\nChecking specific guests:")
for guest in guests_to_check:
    if guest in checked_in:
        print(f"{guest} is checked in.")
    else:
        print(f"{guest} is not checked in.")