#Harry Robinson
#02-10-2014
#Password programme

import random

passwordLength = int(input("Enter the length of your desired password: "))
password = ''
for index in range (0, passwordLength):
    password = password + chr(random.randrange(48,57 and 65,90 and 97,122))
    #print(password)
print(password)
    
