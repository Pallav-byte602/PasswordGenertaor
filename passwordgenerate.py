import random
import string
def gp(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    pwd=""
    meets_requirements=False
    has_number=False
    has_special=False
    while not meets_requirements or len(pwd) <min_length:
        new_char=random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        meets_requirements=True
        if numbers:
            meets_requirements=has_number
        if special_characters:
            meets_requirements=meets_requirements and has_special
    return pwd
min_length=int(input("Enter the minimum length:"))
has_number=input("Do you want to add numbers (y/n)?").lower()=="y"
has_special=input("Do you want to add characters (y/n)?").lower()=="y"
pwd=gp(min_length,has_number,has_special)
print("The generated password:",pwd)          