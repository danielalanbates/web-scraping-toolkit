try:
    with open("Axolotl_Care_Checklist.txt", "r") as file:
        lines = file.readlines()

        clean_lines = []
        for line in lines:
            clean_line = line.strip().lstrip('-")')
            clean_lines.append(clean_line)
        
        clean_lines.sort()
        
        paragraph = ' '.join(clean_lines)
        print(paragraph.upper())

except FileNotFoundError:
    print("Error: The file 'Axolotl_Care_Checklist.txt' was not found.")
    print("Please make sure the script is in the same directory as the text file.")