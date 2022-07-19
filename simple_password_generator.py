import numbers
import random as r
import string as s

first = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) +r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
second = r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters) + r.choice(s.ascii_letters)
n = r.randint(1,9)+r.randint(1,9)+r.randint(1,9)+r.randint(1,9)
m = r.randint(1,9)+r.randint(1,9)+r.randint(1,9)+r.randint(1,9)
number1 =str(n)
number2=str(m)
special_characters = "!","#","$","%","&","*","+","-","/",":",";","<","=",">","?","@","[","]","^","_","{","|","}","~"
special_Characters = r.choice(special_characters)

print("Welcome to simple password generator.\n You can generate safe password for any use.\n===Full forms of some words used===\n 1,y/n = yes/no \n 2, S/E = Start/End") 

password = (number2+first+special_Characters+second+number2)

nickname=input("Do you want to add any nickname (y/n) :")

if nickname == 'y': 
    nickname2=(input("enter nickname :"))
    print("Your password is : ",nickname2+password)
    a= nickname2+password
    b = str(a)
    File = open("Password.txt","w")
    File.write(b)
    File.close()
    
else:
    print("Your Password is :",password)
    a=password
    b = str(a)
    File = open("Password.txt","w")
    File.write(b)
    File.close()
