import re

#email=input("Enter your email").strip()
email="mailar@mailar.edu"
email="mailar@@mailar.edu" # not valid 
email="dfsd email@mailar.edu" # valid too

if re.search(r"^\w+@(\w\.)*\w+\.(com|edu|org)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Not valid")