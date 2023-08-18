with open("names.txt") as file: # read is default mode 
    for line in sorted(file,reverse=True):  
        print("hello," , line.rstrip())
    