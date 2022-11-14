import random
import string as s
import numbers

FirstN = random.randint(1, 9)+random.randint(1, 9)
FrstUsrN = random.choice(s.ascii_letters)+random.choice(s.ascii_letters)+random.choice(s.ascii_letters)+random.choice(s.ascii_letters)

SpChartr = random.choice(s.punctuation)

SndUsrN = random.choice(s.ascii_letters)+random.choice(s.ascii_letters)+random.choice(s.ascii_letters)+random.choice(s.ascii_letters)
LastN = random.randint(1, 9)+random.randint(1, 9)

FrstN = str(FirstN)
SndN = str(LastN)

password = (FrstN+FrstUsrN+SpChartr+SndUsrN+SndN)
print(password)

File = open("Password.txt",'a')
string=str(password)
File.write("\n"+ string)
File.close()
