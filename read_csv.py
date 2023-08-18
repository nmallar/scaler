with open("names.csv") as csvfile:
    for line in csvfile:
        name, house=line.rstrip().split(",")
        print(f"{name},{house}")