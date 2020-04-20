import random
print ("Would you like to play the game (yes/no)?\n")

x =input()

if x == "yes":
    pla_1 = input("Player 1,enter your name: ")
    pla_2 = input("Player 2,enter your name: ")
    

    print("\nWelcome to Dice roll game, player1 name is ",pla_1)
    print("Welcome to Dice roll game, player1 name is ",pla_2)

    print("\n",pla_1 ,"do you want to roll the dice (y/n)")
    x = input()
    b = 0
    e = 0
    if x == "y":
        while True:
            a = 0
            d = 0
            a = int(random.randint(1,6))
            print (pla_1, ",U have rolled: ",a)
            d = int(random.randint(1,6))
            print (pla_2, ",U have rolled: ",d,"\n")
            b = b + a
            e = e + d
            
            if b >= 30 or e >= 30:
               break
        if b > e:
            print (pla_1, "is WINNER!!!\n")
        else:
            print (pla_2, "is WINNER!!!\n")
        print (pla_1," your score is :",b ,pla_2," \nyour socre is: ", e)
    else:
        print(pla_2 ,"do you want to roll the dice (y/n)")
        x = input()
        b = 0
        e = 0
        if x == "y":
            while True:
                a = 0
                d = 0
                a = int(random.randint(1,6))
                print (pla_1, ",U have rolled: ",a)
                d = int(random.randint(1,6))
                print (pla_2, ",U have rolled: ",d,"\n")
                b = b + a
                e = e + d
                
                if b >= 30 or e >= 30:
                   break
            if b > e:
                print (pla_1, "is WINNER!!!\n")
            else:
                print (pla_2, "is WINNER!!!\n")
            print (pla_1," your score is :",b ,pla_2," \nyour socre is: ", e)
else :
    print ("Game ended")

































    
