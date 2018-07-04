import random
import string
import os

# pwd = ""

count1 = 0
length = int(input("How many characters do you want? : "))
leil = 100
amount = int(input("How many passwords would you like? : "))
filName = str(input("What do you want to name the file?"))


def pwd(pword, count, count1):

    while count != length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        everything = lower + num + upper

        pword += random.choice(everything)
        count += 1
        continue

    if count == length:
        with open(filName+'.txt', 'a') as the_file:
            the_file.write(pword + '\n')
        count1 += 1


for i in range(0, amount):
    pwd("", 0, 0)

input('Finished! Press return to exit!')

if count1 == amount:
    os.system('pause')
