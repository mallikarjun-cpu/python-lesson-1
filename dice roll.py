import random

min = 1
max = 6

print("the dice is rolling")
#x = int(random.randint(min,max))

#print (x)

#print ("would you like to roll the dice again?(yes/no)")

y = 'yes'

while True:
    if y == 'yes' :
        a = int(random.randint(min,max))
        print (a)
        print ("would you like to roll the dice again?(yes/no)")
        y = input()
    else:
        break
print ("Game ended, thanks for playing.")
