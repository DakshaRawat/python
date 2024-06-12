rint("Enter multiple lines of text (press Enter on an empty line to finish):") 
lines = [] 
while True: 

    line = input()   

    if line == "":   

        break 

    lines.append(line)   

 

 

print("\nYou entered:") 

for line in lines: 

    print(line) 