#Random password generator

import random
import string
passlen=int(input("enter the length for your password:"))
values=string.ascii_letters+string.digits+string.punctuation
result="".join(random.choice(values) for i in range(passlen))

password=""
for i in range(passlen):
   password+= random.choice(values)

print("Your random password is:",password)

