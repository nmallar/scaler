import csv
name=input("whats your name: ?")
home=input("Whats your home ?")
city='blr'
with open("names_with_header.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","home","city"])
    writer.writerow({"home":home,"name":name,"city":city})
    
    