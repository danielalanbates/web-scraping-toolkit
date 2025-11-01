import os
import datetime

while True:
    # Prompt the user for a filename until they provide one
    filename = input("Enter the filename to search for or 'quit': ")
    if filename.strip() == "" or filename.strip() == "quit" or filename.strip() == "exit":
        print("Exiting the program.")
        exit()
    if os.path.exists(filename):
        print(f"File exists: {filename}")
        print(f"File size (bytes): {os.path.getsize(filename)}")
        timestamp = os.path.getmtime(filename)
        mod_time = datetime.datetime.fromtimestamp(timestamp)
        print(f"Last modified: {mod_time}")
        print(f"Absolute path: {os.path.abspath(filename)}")
        print("-" * 30)
    else:
        print(f"Error: The file \"{filename}\" does not exist.")
    
# Convert the modification time to a readable format
if os.path.exists(filename):
    timestamp = os.path.getmtime(filename)
    print("\n datetime.datetime.fromtimestamp(timestamp)")
    print(os.path.abspath(filename))