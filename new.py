import random as r
import string as s


first_Phase = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) +r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
second_Phase = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
special_characters = " ","!",'"',"#","$","%","&","'",")","(","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"
special_Characters = r.choice(special_characters)
print("Password is ", first_Phase+special_Characters+second_Phase)

nickname=input("Do you want to add any nickname (y/n) :")
if nickname == 'y': 
    nickname2(input("enter nickname \n :"))
Special_Characters=input("need any special characters? (y/n) \n enter: ")