import random as r
import string as s

first = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) +r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
second = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
special_characters = "!","#","$","%","&","*","+","-","/",":",";","<","=",">","?","@","[","]","^","_","{","|","}","~"
special_Characters = r.choice(special_characters)

print("Welcome to simple password generator.\n You can generate safe password for any use.\n===Full forms of some words used===\n 1,y/n = yes/no \n 2, S/E = Start/End") 

nickname=input("Do you want to add any nickname (y/n) :")
if nickname == 'y': 
    nickname2=(input("enter nickname :"))
    nickname_Place =input("Where do you want your nickname to be in (s/e)")
    if nickname_Place == 's':
        print("Your password is :", nickname2+first+special_Characters+second)
    elif nickname_Place == "e":
        print("Your password is :",first+special_Characters+nickname2)
else:
    print("Your Password is :",first+special_Characters+second)


