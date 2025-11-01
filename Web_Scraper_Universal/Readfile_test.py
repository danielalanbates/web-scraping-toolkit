try:
    with open("Axolotl_Care_Checklist.txt", "r") as file:
        lines = file.readlines()

    print("--- Starting Debug Test ---")
    for line in lines:
        print(f"Before: '{line.strip()}'")
        clean_line = line.strip()
        print(f"After:  '{clean_line}'")
        print("--------------------") # Separator for clarity

except FileNotFoundError:
    print("Error: The file 'Axolotl_Care_Checklist.txt' was not found.")