import random

li_m = int(input("Enter the number of times you would like to guess the number: "))

s_n = int(input("Enter starting number: "))
e_n = int(input("Enter ending number: "))

while s_n >= e_n:
    print("you have given negative range!!\n")
    s_n = int(input("Enter starting number: "))
    e_n = int(input("Enter ending number: "))

     


r = int(random.randint(s_n,e_n))
#print("random no is:",r)

i = 0
while i < li_m:
    print("Guess",i+1," ,guess a number between",s_n," and" , e_n)
    g = int(input())
    if g == r:
        break
    elif g > r:
        print("you entered wrong number and its high,.")
    else:
        print("you entered wrong number and its low,.")
    i += 1

print("You have won with just", i+1, "guesses.!")
